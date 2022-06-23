//Funtion for Single Table.

#include <stdio.h>
int printTable(int number)
{
	int counter, product;
	printf("Table Number: %d\n", number);
	for(counter = 1; counter <= 10; counter++)
	{
		product = number * counter;
		printf("%2d X %2d = %3d\n", number, counter, product);
	}
}