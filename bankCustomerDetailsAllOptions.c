//CRUDS Project. (Create, Read, Update, Delete, Search).

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Tools.c"
#define MAXLENGTH 50
#define FILENAME "bank99CustomesDetails.txt"
struct bankCustomerDetails
{
	char accountNumber[25];
	char name[MAXLENGTH];
	float balanceAmount;
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
				createBankCustomerDetails();
				break;
			case 2:
				displayBankCustomerDetails();
				break;
			case 3:
				searchCustomerDetails();
				break;
			case 4:
				updateCustomerDetails();
				break;
			case 5:
				deleteCustomerDetails();
				break;	
			default:
				printf("Exit!");
				exit(0);
		}
	} while (option != 5);
}
int createBankCustomerDetails()
{
	int confirmation;
	FILE *fpCustomerDetails;
	fpCustomerDetails = fopen(FILENAME, "a");
	if(fpCustomerDetails == NULL)
	{
		printf("Error in opening.\n");
		exit(0);
	}
	struct bankCustomerDetails customerDetails;
	do
	{
		fflush(stdin);
		printf("Enter Account Number: ");
		fgets(customerDetails.accountNumber, 25, stdin);
		remove_newline(customerDetails.accountNumber);
		printf("Enter Customer Name: ");
		fgets(customerDetails.name, MAXLENGTH, stdin);
		remove_newline(customerDetails.name);
		printf("Enter Balance Amount: ");
		scanf("%f", &customerDetails.balanceAmount);
		customerDetails.accountStatus = 1;
		fwrite(&customerDetails, sizeof(customerDetails), 1, fpCustomerDetails);
		printf("Do you want to continue?\n1. Yes = 1.\n2. No = 2\nChoose(1 or 2): ");
		scanf("%d", &confirmation);
	} while (confirmation != 2);
	fclose(fpCustomerDetails);
	return 0;
}
int displayBankCustomerDetails()
{
	struct bankCustomerDetails customerDetails;
	FILE *fpCustomerDetails;
	fpCustomerDetails = fopen(FILENAME, "r");
	if (fpCustomerDetails == NULL)
	{
		printf("Error in opening.\n");
		exit(0);
	}
	if (fread(&customerDetails, sizeof(customerDetails), 1, fpCustomerDetails) == 0)
	{
		printf("No record found.\n");
	}
	do 
	{
		printf("Account Number: %s\n", customerDetails.accountNumber);
		printf("Customer Name: %s\n", customerDetails.name);
		printf("Balance Amount: %f\n", customerDetails.balanceAmount);
		if (customerDetails.accountStatus == 0)
		{
			printf("Account Closed.\n");
		}
		else
		{
			printf("Active Account.\n");
		}
	 } while (fread(&customerDetails, sizeof(customerDetails), 1, fpCustomerDetails) == 1);
	fclose(fpCustomerDetails);
	return 0;
}
int searchCustomerDetails()
{
	char Id[25];
	int recordStatus = 1;
	struct bankCustomerDetails customerDetails;
	FILE *fpCustomerDetails;
	fpCustomerDetails = fopen(FILENAME, "r");
	if (fpCustomerDetails == NULL)
	{
		printf("Error in opening.\n");
		exit(0);
	}
	printf("Enter Account Number to search: ");
	scanf("%s", &Id);
	while ((fread(&customerDetails, sizeof(customerDetails), 1, fpCustomerDetails) == 1) && recordStatus == 1)
	{
		if (strstr(Id, customerDetails.accountNumber) != NULL)
		{
			recordStatus = 0;
			printf("Account Number: %s\n", customerDetails.accountNumber);
			printf("Customer Name: %s\n", customerDetails.name);
			printf("Balance Amount: %f\n", customerDetails.balanceAmount);
			if (customerDetails.accountStatus == 0)
			{
				printf("Account Closed.\n");
			}
			else
			{
				printf("Active Account.\n");
			}
		}	
	}
	if ((fread(&customerDetails, sizeof(customerDetails), 1, fpCustomerDetails) == 0) && recordStatus == 1)
	{
		printf("No record found.\n");
	}
	fclose(fpCustomerDetails);
	return 0;
}
int updateCustomerDetails()
{
	char accountNumberToSearch[25];
	int recordStatus = 0;
	FILE *fpCustomerDetails;
	fpCustomerDetails = fopen(FILENAME, "r+");
	struct bankCustomerDetails customerDetails;
	if(fpCustomerDetails == NULL)
	{
		printf("Error found in opening.\n");
		exit(0);
	}
	printf("Enter accountNumber to search: ");
	scanf("%s", &accountNumberToSearch);
	fflush(stdin);
	while ((fread(&customerDetails, sizeof(customerDetails), 1, fpCustomerDetails) == 1) && recordStatus == 0)
	{
		if (strstr(accountNumberToSearch, customerDetails.accountNumber) != NULL)
		{
			fseek(fpCustomerDetails, ((-1) * sizeof(customerDetails)), SEEK_CUR);
			recordStatus = 1;
			printf("Enter Customer Name: ");
			fgets(customerDetails.name, MAXLENGTH, stdin);
			remove_newline(customerDetails.name);
			printf("Enter Balance Amount: ");
			scanf("%f", &customerDetails.balanceAmount);
			fwrite(&customerDetails, sizeof(customerDetails), 1, fpCustomerDetails);
			fseek(fpCustomerDetails, sizeof(customerDetails), SEEK_END);
		}
	}
	if ((fread(&customerDetails, sizeof(customerDetails), 1, fpCustomerDetails) == 0) && (recordStatus == 0))
	{
		printf("No record found.\n");
	}
	fclose(fpCustomerDetails);
	return 0;
}
int deleteCustomerDetails()
{
	char accountNumberToSearch[25];
	int recordStatus = 0;
	FILE *fpCustomerDetails;
	fpCustomerDetails = fopen(FILENAME, "r+");
	struct bankCustomerDetails customerDetails;
	if(fpCustomerDetails == NULL)
	{
		printf("Error found in opening.\n");
	}
	printf("Enter accountNumber to search: ");
	scanf("%s", &accountNumberToSearch);
	while ((fread(&customerDetails, sizeof(customerDetails), 1, fpCustomerDetails) == 1) && recordStatus == 0)
	{
		if (strstr(accountNumberToSearch, customerDetails.accountNumber) != NULL)
		{
			fseek(fpCustomerDetails, ((-1) * sizeof(customerDetails)), SEEK_CUR);
			recordStatus = 1;
			customerDetails.accountStatus = 0;
			fwrite(&customerDetails, sizeof(customerDetails), 1, fpCustomerDetails);
			fseek(fpCustomerDetails, sizeof(customerDetails), SEEK_END);
		}
	}
	if ((fread(&customerDetails, sizeof(customerDetails), 1, fpCustomerDetails) == 0) && (recordStatus == 1))
	{
		printf("No record found.\n");
	}
	fclose(fpCustomerDetails);
	return 0;
}

