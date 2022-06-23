//Read and save a bank customer details. (fwrite())

#include <stdio.h>
#include <stdlib.h>
#define FILE_NAME "bankCustomerdetails.dat"
struct bank_customer_details
{
	char name[50], gender[10];
	int account_number, start_account_year, age;
	float balance;
};
int main()
{
	int number_of_customers, customer_counter, number_of_files;
	FILE *file_pointer;
	file_pointer = fopen(FILE_NAME, "wb");
	if(file_pointer == NULL)
	{
		printf("Error opening file\n");
		exit(1);
	}
	printf("Testing fwrite() function: \n\n");
	printf("Enter the number of records do you want to enter: ");
	scanf("%d", &number_of_customers);
	struct bank_customer_details customer_details[number_of_customers];
	for(customer_counter = 0; customer_counter < number_of_customers; customer_counter++)
	{
		printf("\nEnter details of customer %d:\n", customer_counter + 1);
		printf("Customer Name: ");
		scanf("%s", customer_details[customer_counter].name);
		printf("Account Number: ");
		scanf("%d", &customer_details[customer_counter].account_number);
		printf("Bank Balance: ");
		scanf("%f", &customer_details[customer_counter].balance);
		printf("Gender: ");
		scanf("%s", customer_details[customer_counter].gender);
		printf("Age: ");
		scanf("%d", &customer_details[customer_counter].age);
		printf("Account Opened in the year: ");
		scanf("%d", &customer_details[customer_counter].start_account_year);

		number_of_files = fwrite(&customer_details, sizeof(customer_details), 1, file_pointer);
		printf("Number of items written to the file: %d\n", number_of_files);
	}
	fclose(file_pointer);
	return 0;
}