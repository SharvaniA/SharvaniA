// Single Multiplication Table.

#include <stdio.h>
#include "functionSingleTable.c"
int main()
{
	int number, counter, product;
	printf("Enter a number to print its multiplication table: ");
	scanf("%d", &number);
	printTable(number);
}
