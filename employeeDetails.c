//CRUDS Project. (Create, Read, Update, Delete, Search).

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Tools.c"
#define MAXLENGTH 50
#define FILENAME "employeeDetails72.txt"
struct employeeBasicDetails
{
	char employeeId[15];
	char employeeName[MAXLENGTH];
	float employeeSalary;
	int employeeStatus;
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
				creteEmployeeDetails();
				break;
			case 2:
				displayEmployeeDetails();
				break;
			case 3:
				searchEmployeeDetails();
				break;
			case 4:
				updateEmployeeDetails();
				break;
			case 5:
				deleteEmployeeDetails();
				break;	
			case 6:
				printf("Exit!");
				exit(0);
		}
	} while (option != 6);
}

int creteEmployeeDetails()
{
	int confirmation;
	FILE *fpEmployeeDetails;
	fpEmployeeDetails = fopen(FILENAME, "a");
	if(fpEmployeeDetails == NULL)
	{
		printf("Error in opening.\n");
		exit(0);
	}
	struct employeeBasicDetails employeeDetails;
	do
	{
		fflush(stdin);
		printf("Enter Employee Id: ");
		fgets(employeeDetails.employeeId, 15, stdin);
		remove_newline(employeeDetails.employeeId);
		printf("Enter Employee Name: ");
		fgets(employeeDetails.employeeName, MAXLENGTH, stdin);
		remove_newline(employeeDetails.employeeName);
		fflush(stdin);
		printf("Enter Employee Salary: ");
		scanf("%f", &employeeDetails.employeeSalary);
		employeeDetails.employeeStatus = 1;
		fwrite(&employeeDetails, sizeof(employeeDetails), 1, fpEmployeeDetails);
		printf("Do you want to continue?\n1. Yes = 1.\n2. No = 2\nChoose(1 or 2): ");
		scanf("%d", &confirmation);
	} while (confirmation != 2);
	fclose(fpEmployeeDetails);
	return 0;
}
int displayEmployeeDetails()
{
	struct employeeBasicDetails employeeDetails;
	FILE *fpEmployeeDetails;
	fpEmployeeDetails = fopen(FILENAME, "r");
	if(fpEmployeeDetails == NULL)
	{
		printf("Error in opening.\n");
		exit(0);
	}
	if (fread(&employeeDetails, sizeof(employeeDetails), 1, fpEmployeeDetails) == 0)
	{
		printf("No record found.\n");
	}
	do 
	{
		printf("Enter Employee Id: %s\n", employeeDetails.employeeId);
		printf("Enter Employee Name: %s\n", employeeDetails.employeeName);
		printf("Enter Employee Salary: %f\n", employeeDetails.employeeSalary);
		if (employeeDetails.employeeStatus == 0)
		{
			printf("Resigned.\n");
		}
		else
		{
			printf("Working.\n");
		}
	 } while (fread(&employeeDetails, sizeof(employeeDetails), 1, fpEmployeeDetails) == 1);
	fclose(fpEmployeeDetails);
	return 0;
}
int searchEmployeeDetails()
{
	char Id[25];
	int recordStatus = 1;
	struct employeeBasicDetails employeeDetails;
	FILE *fpEmployeeDetails;
	fpEmployeeDetails = fopen(FILENAME, "r");
	if(fpEmployeeDetails == NULL)
	{
		printf("Error in opening.\n");
		exit(0);
	}
	printf("Enter Employee Id to search: ");
	scanf("%s", &Id);
	while ((fread(&employeeDetails, sizeof(employeeDetails), 1, fpEmployeeDetails) == 1) && recordStatus == 1)
	{
		if (strstr(Id, employeeDetails.employeeId) != NULL)
		{
			recordStatus = 0;
			printf("Enter Employee Id: %s\n", employeeDetails.employeeId);
			printf("Enter Employee Name: %s\n", employeeDetails.employeeName);
			printf("Enter Employee Salary: %f\n", employeeDetails.employeeSalary);
			if (employeeDetails.employeeStatus == 0)
			{
				printf("Resigned.\n");
			}
			else
			{
				printf("Working.\n");
			}
		}	
	}
	if ((fread(&employeeDetails, sizeof(employeeDetails), 1, fpEmployeeDetails) == 0) && recordStatus == 1)
	{
		printf("No record found.\n");
	}
	fclose(fpEmployeeDetails);
	return 0;
}
int updateEmployeeDetails()
{
	char employeeIdToSearch[25];
	int recordStatus = 0;
	FILE *fpEmployeeDetails;
	fpEmployeeDetails = fopen(FILENAME, "r+");
	struct employeeBasicDetails employeeDetails;
	if(fpEmployeeDetails == NULL)
	{
		printf("Error in opening.\n");
		exit(0);
	}
	printf("Enter Employee Id to search: ");
	scanf("%s", &employeeIdToSearch);
	fflush(stdin);
	while ((fread(&employeeDetails, sizeof(employeeDetails), 1, fpEmployeeDetails) == 1) && recordStatus == 0)
	{
		if (strstr(employeeIdToSearch, employeeDetails.employeeId) != NULL)
		{
			fseek(fpEmployeeDetails, ((-1) * sizeof(employeeDetails)), SEEK_CUR);
			recordStatus = 1;
			printf("Enter Employee Name: ");
			fgets(employeeDetails.employeeName, MAXLENGTH, stdin);
			remove_newline(employeeDetails.employeeName);
			printf("Enter Employee Salary: ");
			scanf("%f", &employeeDetails.employeeSalary);
			fwrite(&employeeDetails, sizeof(employeeDetails), 1, fpEmployeeDetails);
			break;
		}
	}
	if ((fread(&employeeDetails, sizeof(employeeDetails), 1, fpEmployeeDetails) == 0) && (recordStatus == 0))
	{
		printf("No record found.\n");
	}
	fclose(fpEmployeeDetails);
	return 0;
}
int deleteEmployeeDetails()
{
	char employeeIdToSearch[25];
	int recordStatus = 0;
	FILE *fpEmployeeDetails;
	fpEmployeeDetails = fopen(FILENAME, "r+");
	struct employeeBasicDetails employeeDetails;
	if(fpEmployeeDetails == NULL)
	{
		printf("Error in opening.\n");
		exit(0);
	}
	printf("Enter Employee Id to search: ");
	scanf("%s", &employeeIdToSearch);
	fflush(stdin);
	while ((fread(&employeeDetails, sizeof(employeeDetails), 1, fpEmployeeDetails) == 1) && recordStatus == 0)
	{
		if (strstr(employeeIdToSearch, employeeDetails.employeeId) != NULL)
		{
			fseek(fpEmployeeDetails, ((-1) * sizeof(employeeDetails)), SEEK_CUR);
			recordStatus = 1;
			employeeDetails.employeeStatus = 0;
			fwrite(&employeeDetails, sizeof(employeeDetails), 1, fpEmployeeDetails);
			break;
		}
	}
	if ((fread(&employeeDetails, sizeof(employeeDetails), 1, fpEmployeeDetails) == 0) && (recordStatus == 0))
	{
		printf("No record found.\n");
	}
	fclose(fpEmployeeDetails);
	return 0;
}