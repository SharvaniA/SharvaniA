//Student details.


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Tools.c"
#define MAXLENGTH 50
#define FILENAME "studentDetails279.txt"
struct studentPersonalDetails
{
	char admissionNumber[6];
	char studentName[MAXLENGTH];
	char phoneNumber[MAXLENGTH];
	float amountPaid;
	int status;
};

int main()
{
	show_menu();
}

int show_menu()
{
	int option;
	do
	{
		printf("Select the below option to proceed:\n1. Save Details.\n2. Show Details.\n3. Search Details.\n4. Update Details.\n5. Delete Details.\n6. Exit\n");
		printf("Choose(1, 2, 3, 4, 5 or 6): ");
		scanf("%d", &option);
		switch(option)
		{
			case 1:
				createStudentDetails();
				break;
			case 2:
				displayStudentDetails();
				break;
			case 3:
				searchStudentDetails();
				break;
			case 4:
				updateStudentDetails();
				break;
			case 5:
				deleteStudentDetails();
				break;
			default:
				printf("Exit!");
				exit(0);
		}
	} while (option != 6);
}

int createStudentDetails()
{
	int confirmation;
	FILE *fpStudentDetails;
	fpStudentDetails = fopen(FILENAME, "a");
	if (fpStudentDetails == NULL)
	{
		printf("Error in opening.\n");
		exit(0);
	}
	struct studentPersonalDetails studentDetails;
	do
	{
		fflush(stdin);
		printf("Enter Student Admission Number: ");
		fgets(studentDetails.admissionNumber, 6, stdin);
		remove_newline(studentDetails.admissionNumber);
		printf("Enter Student Name: ");
		fgets(studentDetails.studentName, MAXLENGTH, stdin);
		remove_newline(studentDetails.studentName);
		printf("Enter Parent Mobile Number: ");
		fgets(studentDetails.phoneNumber, MAXLENGTH, stdin);
		remove_newline(studentDetails.phoneNumber);
		fflush(stdin);
		printf("Enter Amount Paid: ");
		scanf("%f", &studentDetails.amountPaid);
		studentDetails.status = 1;
		fwrite(&studentDetails, sizeof(studentDetails), 1, fpStudentDetails);
		printf("Do you want to continue?\n1. Yes = 1.\n2. No = 2\nChoose(1 or 2): ");
		scanf("%d", &confirmation);
	} while (confirmation != 2);
	fclose(fpStudentDetails);
	return 0;
}

int displayStudentDetails()
{
	struct studentPersonalDetails studentDetails;
	FILE *fpStudentDetails;
	fpStudentDetails = fopen(FILENAME, "r");
	if (fpStudentDetails == NULL)
	{
		printf("Error in opening.\n");
		exit(0);
	}
	do 
	{
		printf("Admission Number: %s\n", studentDetails.admissionNumber);
		printf("Student Name: %s\n", studentDetails.studentName);
		printf("Mobile Number: %s\n", studentDetails.phoneNumber);
		printf("Amount Paid: %f\n", studentDetails.amountPaid);
		if (studentDetails.status == 0)
		{
			printf("Admission Cancelled.\n");
		}
		else
		{
			printf("Adimission Successfull.\n");
		}
	 } while (fread(&studentDetails, sizeof(studentDetails), 1, fpStudentDetails) == 1);
	fclose(fpStudentDetails);
	return 0;
}

int searchStudentDetails()
{
	char Id[6];
	int recordStatus = 1;
	struct studentPersonalDetails studentDetails;	
	FILE *fpStudentDetails;
	fpStudentDetails = fopen(FILENAME, "r");
	if (fpStudentDetails == NULL)
	{
		printf("Error in opening.\n");
		exit(0);
	}
	printf("Enter Admission Number to search: ");
	scanf("%s", &Id);
	while ((fread(&studentDetails, sizeof(studentDetails), 1, fpStudentDetails) == 1) && recordStatus == 1)
	{
		if (strstr(Id, studentDetails.admissionNumber) != NULL)
		{
			recordStatus = 0;
			printf("Admission Number: %s\n", studentDetails.admissionNumber);
			printf("Student Name: %s\n", studentDetails.studentName);
			printf("Mobile Number: %s\n", studentDetails.phoneNumber);
			printf("Amount Paid: %f\n", studentDetails.amountPaid);
			if (studentDetails.status == 0)
			{
				printf("Admission Cancelled.\n");
			}
			else
			{
				if (studentDetails.status == 1)
				{
					printf("Adimission Successfull.\n");
				}
			}
			break;
		}	
	}
	if ((fread(&studentDetails, sizeof(studentDetails), 1, fpStudentDetails) == 0) && recordStatus == 1)
	{
		printf("No record found.\n");
	}
	fclose(fpStudentDetails);
	return 0;
}

int updateStudentDetails()
{
	char admissionNumberToSearch[25];
	int recordStatus = 0;
	FILE *fpStudentDetails;
	fpStudentDetails = fopen(FILENAME, "r+");
	struct studentPersonalDetails studentDetails;	
	if(fpStudentDetails == NULL)
	{
		printf("Error found in opening.\n");
		exit(0);
	}
	printf("Enter accountNumber to search: ");
	scanf("%s", &admissionNumberToSearch);
	fflush(stdin);
	while ((fread(&studentDetails, sizeof(studentDetails), 1, fpStudentDetails) == 1) && recordStatus == 0)
	{
		if (strstr(admissionNumberToSearch, studentDetails.admissionNumber) != NULL)
		{
			fseek(fpStudentDetails, ((-1) * sizeof(studentDetails)), SEEK_CUR);
			recordStatus = 1;
			printf("Enter Student Name: ");
			fgets(studentDetails.studentName, MAXLENGTH, stdin);
			remove_newline(studentDetails.studentName);
			printf("Enter Parent Mobile Number: ");
			fgets(studentDetails.phoneNumber, MAXLENGTH, stdin);
			remove_newline(studentDetails.phoneNumber);
			printf("Enter Amount Paid: ");
			scanf("%f", &studentDetails.amountPaid);
			fwrite(&studentDetails, sizeof(studentDetails), 1, fpStudentDetails);
			break;
		}
	}
	if (recordStatus == 0)
	{
		printf("No record found.\n");
	}
	fclose(fpStudentDetails);
	return 0;
}

int deleteStudentDetails()
{
	char admissionNumberToSearch[6];
	int recordStatus = 0;
	FILE *fpStudentDetails;
	fpStudentDetails = fopen(FILENAME, "r+");
	struct studentPersonalDetails studentDetails;
	if(fpStudentDetails == NULL)
	{
		printf("Error found in opening.\n");
		exit(0);
	}
	printf("Enter Admission Number to search: ");
	scanf("%s", &admissionNumberToSearch);
	while ((fread(&studentDetails, sizeof(studentDetails), 1, fpStudentDetails) == 1) && recordStatus == 0)
	{
		if (strstr(admissionNumberToSearch, studentDetails.admissionNumber) != NULL)
		{
			fseek(fpStudentDetails, ((-1) * sizeof(studentDetails)), SEEK_CUR);
			recordStatus = 1;
			studentDetails.status = 0;
			fwrite(&studentDetails, sizeof(studentDetails), 1, fpStudentDetails);
			break;
		}
	}
	if (recordStatus == 1)
	{
		printf("No record found.\n");
	}
	fclose(fpStudentDetails);
	return 0;
}