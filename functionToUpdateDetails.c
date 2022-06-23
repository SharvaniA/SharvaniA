//Function to update details.

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