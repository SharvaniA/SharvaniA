 // Printing Multiplication table for the given number.

#include <stdio.h>
int main()
{
	int number, counter, product;
	printf("Enter a number to print its multiplication tabele: ");
	scanf("%d", &number);
	for (counter = 1; counter <= 10; counter++)
	{
		product = counter * number;
		printf("%2d X %2d = %3d \n", number, counter, product);
	}
}