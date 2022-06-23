//Function to create file.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define FILENAME "Hello.txt"
#include "Tools.c"
#define MAXLENGTH 50
struct bankCustomerDetails
{
	char accountNumber;
	char name[MAXLENGTH];
	float balanceAmount;
};
int main()
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
		scanf("%c", &customerDetails.accountNumber);
		fflush(stdin);
		printf("Enter Customer Name: ");
		fgets(customerDetails.name, MAXLENGTH, stdin);
		remove_newline(customerDetails.name);
		printf("Enter Balance Amount: ");
		scanf("%f", &customerDetails.balanceAmount);
		fwrite(&customerDetails, sizeof(customerDetails), 1, fpCustomerDetails);
		printf("Do you want to continue?\n1. Yes = 1.\n2. No = 2\nChoose(1 or 2): ");
		scanf("%d", &confirmation);
	} while (confirmation != 2);
	fclose(fpCustomerDetails);
	return 0;
}