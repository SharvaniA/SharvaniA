//Function to search record.


struct bankCustomerDetails
{
	char accountNumber;
	char name[MAXLENGTH];
	float balanceAmount;
};
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
		}	
	}
	if ((fread(&customerDetails, sizeof(customerDetails), 1, fpCustomerDetails) == 1) && recordStatus == 1)
	{
		printf("No record found.\n");
	}
	fclose(fpCustomerDetails);
	return 0;
}
