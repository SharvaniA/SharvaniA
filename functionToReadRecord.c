//Function to read record.

#include FILENAME ......
struct bankCustomerDetails
{
	char accountNumber;
	char name[MAXLENGTH];
	float balanceAmount;
};

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
	 } while (fread(&customerDetails, sizeof(customerDetails), 1, fpCustomerDetails) == 1);
	fclose(fpCustomerDetails);
	return 0;
}