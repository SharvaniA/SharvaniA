//Creating menu type program for Bank Customer details.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGTH 30
#define FILE_NAME "bankCustomerdetails.dat"
#include "removeNewlineFunction.c"
struct bank_customer_details
{
	char account_number[MAX_LENGTH]; 
	char name[MAX_LENGTH];
	char gender;
	int age;
	float balance;
	int start_account_year;
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
		printf("Select the below option to proceed:\n1. Save Details.\n2. Show Details.\n3. Exit.\n");
		printf("Choose(1, 2 or 3): ");
		scanf("%d", &option);
		switch(option)
		{
			case 1:
				save_bank_customer_details();
				break;
			case 2:
				show_bank_customer_details();
				break;
			default:
				printf("Exit!");
				exit(0);
		}
	} while (option != 3);
}

int save_bank_customer_details()
{
	int customer_counter;
	FILE *fp_bank_customer;
	fp_bank_customer = fopen(FILE_NAME, "a");
	if(fp_bank_customer == NULL)
	{
		printf("Error opening file\n");
		exit(1);
	}
	int yes_no;
	struct bank_customer_details customer_details;
	customer_counter = 1;
	do
	{
		printf("\nEnter details of customer %d:\n", customer_counter);
		fflush(stdin);
		printf("Account Number: ");
		scanf("%s", customer_details.account_number);
		fflush(stdin);
		printf("Customer Name: ");
		fgets(customer_details.name, MAX_LENGTH, stdin);
		remove_newline(customer_details.name);
		printf("Bank Balance: ");
		scanf("%f", &customer_details.balance);
		fflush(stdin);
		printf("Gender(F or M): ");
		scanf("%c", &customer_details.gender);
		fflush(stdin);
		printf("Age: ");
		scanf("%d", &customer_details.age);
		printf("Account Opened in the year: ");
		scanf("%d", &customer_details.start_account_year);
		fwrite(&customer_details, sizeof(customer_details), 1, fp_bank_customer);
		customer_counter = customer_counter + 1;
		printf("Do you want to continue?\n1. Yes = 1.\n2. No = 2\n");
		printf("Choose(1 or 2): ");
		scanf("%d", &yes_no);
	} while (yes_no != 2);
	fclose(fp_bank_customer);
	return 0;
}
int show_bank_customer_details()
{
	int customer_counter;
	struct bank_customer_details customer_details;
	FILE *fp_bank_customer;
	fp_bank_customer = fopen(FILE_NAME, "rb");
	if (fp_bank_customer == NULL)
	{
		printf("Error opening file\n");
		exit(1);
	}
	customer_counter = 1;
	while (fread(&customer_details, sizeof(customer_details), 1, fp_bank_customer) == 1)
	{
		printf("\nDetails of customer %d:\n", customer_counter);
		printf("Account Number: %s\n", customer_details.account_number);
		printf("Customer Name: %s\n", customer_details.name);
		printf("Bank Balance: %f\n", customer_details.balance);
		printf("Gender: %c\n", customer_details.gender);
		printf("Age: %d\n", customer_details.age);
		printf("Account Opened in the year: %d\n", customer_details.start_account_year);
		customer_counter = customer_counter + 1;
	}
	fclose(fp_bank_customer);
	return 0;
}
