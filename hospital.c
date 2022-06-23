//CRUDS Project. (Create, Read, Update, Delete, Search).

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Tools.c"
#define MAXLENGTH 50
#define FILENAME "patientEntries99.txt"
struct patientEntries
{
	char patientNumber[15];
	char patientName[MAXLENGTH];
	int amountPaid;
	int accountStatus;
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
				createPatientDetails();
				break;
			case 2:
				displayPatientDetails();
				break;
			case 3:
				searchPatientDetails();
				break;
			case 4:
				updatePatientDetails();
				break;
			case 5:
				deletePatientDetails();
				break;	
			default:
				printf("Exit!");
				exit(0);
		}
	} while (option != 5);
}
int createPatientDetails()
{
	int confirmation;
	FILE *fpPatientDetails;
	fpPatientDetails = fopen(FILENAME, "a");
	if(fpPatientDetails == NULL)
	{
		printf("Error in opening.\n");
		exit(0);
	}
	struct patientEntries patientDetails;
	do
	{
		fflush(stdin);
		printf("Enter Patient Number: ");
		fgets(patientDetails.patientNumber, 15, stdin);
		remove_newline(patientDetails.patientNumber);
		printf("Enter Patient Name: ");
		fgets(patientDetails.patientName, MAXLENGTH, stdin);
		remove_newline(patientDetails.patientName);
		fflush(stdin);
		printf("Enter Amount Paid: ");
		scanf("%d", &patientDetails.amountPaid);
		patientDetails.accountStatus = 1;
		fwrite(&patientDetails, sizeof(patientDetails), 1, fpPatientDetails);
		printf("Do you want to continue?\n1. Yes = 1.\n2. No = 2\nChoose(1 or 2): ");
		scanf("%d", &confirmation);
	} while (confirmation != 2);
	fclose(fpPatientDetails);
	return 0;
}
int displayPatientDetails()
{
	struct patientEntries patientDetails;
	FILE *fpPatientDetails;
	fpPatientDetails = fopen(FILENAME, "r");
	if (fpPatientDetails == NULL)
	{
		printf("Error in opening.\n");
		exit(0);
	}
	if (fread(&patientDetails, sizeof(patientDetails), 1, fpPatientDetails) == 0)
	{
		printf("No record found.\n");
	}
	do 
	{
		printf("Patient Number: %s\n", patientDetails.patientNumber);
		printf("Patient Name: %s\n", patientDetails.patientName);
		printf("Amount Paid: %d\n", patientDetails.amountPaid);
		if (patientDetails.accountStatus == 0)
		{
			printf("Account Closed.\n");
		}
		else
		{
			printf("Active Account.\n");
		}
	 } while (fread(&patientDetails, sizeof(patientDetails), 1, fpPatientDetails) == 1);
	fclose(fpPatientDetails);
	return 0;
}
int searchPatientDetails()
{
	char Id[15];
	int recordStatus = 1;
	struct patientEntries patientDetails;
	FILE *fpPatientDetails;
	fpPatientDetails = fopen(FILENAME, "r");
	if (fpPatientDetails == NULL)
	{
		printf("Error in opening.\n");
		exit(0);
	}
	printf("Enter Patient Number to search: ");
	scanf("%s", &Id);
	while ((fread(&patientDetails, sizeof(patientDetails), 1, fpPatientDetails) == 1) && recordStatus == 1)
	{
		if (strstr(Id, patientDetails.patientNumber) != NULL)
		{
			recordStatus = 0;
			printf("Patient Number: %s\n", patientDetails.patientNumber);
			printf("Patient Name: %s\n", patientDetails.patientName);
			printf("Amount Paid: %d\n", patientDetails.amountPaid);
			if (patientDetails.accountStatus == 0)
			{
				printf("Account Closed.\n");
			}
			else
			{
				printf("Active Account.\n");
			}
			break;
		}	
	}
	if ((fread(&patientDetails, sizeof(patientDetails), 1, fpPatientDetails) == 0) && recordStatus == 1)
	{
		printf("No record found.\n");
	}
	fclose(fpPatientDetails);
	return 0;
}
int updatePatientDetails()
{
	char patientNumberToSearch[15];
	int recordStatus = 0;
	FILE *fpPatientDetails;
	fpPatientDetails = fopen(FILENAME, "r+");
	struct patientEntries patientDetails;
	if(fpPatientDetails == NULL)
	{
		printf("Error found in opening.\n");
		exit(0);
	}
	printf("Enter Patient Number to search: ");
	scanf("%s", &patientNumberToSearch);
	fflush(stdin);
	while ((fread(&patientDetails, sizeof(patientDetails), 1, fpPatientDetails) == 1) && recordStatus == 0)
	{
		if (strstr(patientNumberToSearch, patientDetails.patientNumber) != NULL)
		{
			fseek(fpPatientDetails, ((-1) * sizeof(patientDetails)), SEEK_CUR);
			recordStatus = 1;
			printf("Enter Patient Name: ");
			fgets(patientDetails.patientName, MAXLENGTH, stdin);
			remove_newline(patientDetails.patientName);
			fflush(stdin);
			printf("Enter Amount Paid: ");
			scanf("%d", &patientDetails.amountPaid);
			fwrite(&patientDetails, sizeof(patientDetails), 1, fpPatientDetails);
			break;
		}
	}
	if ((fread(&patientDetails, sizeof(patientDetails), 1, fpPatientDetails) == 0) && (recordStatus == 0))
	{
		printf("No record found.\n");
	}
	fclose(fpPatientDetails);
	return 0;
}
int deletePatientDetails()
{
	char patientNumberToSearch[15];
	int recordStatus = 0;
	FILE *fpPatientDetails;
	fpPatientDetails = fopen(FILENAME, "r+");
	struct patientEntries patientDetails;
	if(fpPatientDetails == NULL)
	{
		printf("Error found in opening.\n");
	}
	printf("Enter patientNumber to search: ");
	scanf("%s", &patientNumberToSearch);
	while ((fread(&patientDetails, sizeof(patientDetails), 1, fpPatientDetails) == 1) && recordStatus == 0)
	{
		if (strstr(patientNumberToSearch, patientDetails.patientNumber) != NULL)
		{
			fseek(fpPatientDetails, ((-1) * sizeof(patientDetails)), SEEK_CUR);
			recordStatus = 1;
			patientDetails.accountStatus = 0;
			fwrite(&patientDetails, sizeof(patientDetails), 1, fpPatientDetails);
			break;
		}
	}
	if ((fread(&patientDetails, sizeof(patientDetails), 1, fpPatientDetails) == 0) && (recordStatus == 1))
	{
		printf("No record found.\n");
	}
	fclose(fpPatientDetails);
	return 0;
}