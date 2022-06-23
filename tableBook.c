// Printing Tables Book

#include <stdio.h>
int main()
{
	int countOfTables, counter, number, product;
	printf("How many tables do you want to print in a tables book? ");
	scanf("%d", &countOfTables);
	printf("Tables Book\n");
	printf("Tables upto: %d\n", countOfTables);
	for(number = 1; number <= countOfTables; number++)
	{
		printf("Table Number: %d\n", number);
		for(counter = 0; counter <= 10; counter++)
		{
			product = number * counter;
			printf("%2d X %2d = %3d\n", number, counter, product); 	
		}
	}
}