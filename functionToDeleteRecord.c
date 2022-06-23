//Function to delete record.

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
			printf("Status: %d\n", customerDetails.deleteStatus = 1);
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