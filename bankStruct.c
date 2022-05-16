//Read and display a bank customer details.

#include <stdio.h>
#include <stdlib.h>
struct bankCustomer 
{
	int accountNumber;
	char name[30];
	float balance;
}
str[6];
int main()
{
	int counter, n;
	printf("Enter number of customers: ");
	scanf("%d", &n);
	for(counter = 0; counter < n; counter++)
	{
		printf("Customer Name: ");
		scanf("%s", &str[counter].name);
		printf("Account Number: ");
		scanf("%d", &str[counter].accountNumber);
		printf("Balance: ");
		scanf("%f", &str[counter].balance);
	}
	for(counter = 0; counter < n; counter++)
	{
		printf("Name: %s\n", str[counter].name);
		printf("Account Number: %d\n", str[counter].accountNumber);
		printf("Balance: %f\n", str[counter].balance);		
	}
}