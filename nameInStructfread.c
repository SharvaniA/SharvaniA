//Display all bank customer details saved in the file.

#include <stdio.h>
#include <stdlib.h>
#define MAX_LENGTH 30
#define FILE_NAME "bankCustomerdetails.dat"
struct bankCustomerdetails
{
	char name[MAX_LENGTH], gender[10];
	int accountNumber, startAccountYear, age;
	float balance;
};
int main()
{
	int customerCounter;
	struct bankCustomerdetails bankCustomer;
	FILE *fpBankCustomer;
	fpBankCustomer = fopen(FILE_NAME, "rb");
	if (fpBankCustomer == NULL)
	{
		printf("Error opening file\n");
		exit(1);
	}
	while (fread(&bankCustomer, sizeof(bankCustomer), 1, fpBankCustomer) == 1)
	{
		printf("\nDetails of customer %d:\n", customerCounter + 1);
		printf("Customer Name: %s\n", bankCustomer.name);
		printf("Account Number: %d\n", bankCustomer.accountNumber);
		printf("Bank Balance: %f\n", bankCustomer.balance);
		printf("Gender: %s\n", bankCustomer.gender);
		printf("Age: %d\n", bankCustomer.age);
		printf("Account Opened in the year: %d\n", bankCustomer.startAccountYear);
	}
	fclose(fpBankCustomer);
	return 0;
}
