// Tables Book with underline.

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "Tools.c"
int main()
{
	int tables_count, table_number, product, table_counter;
	printf("how many tables do you want to print in Tables book?\n");
	scanf("%d", &tables_count);
	if (tables_count > 0)
	{
		print_tables_book(tables_count);
	}
	else
	{
		printf("Enter a valid number.\n");
	}
}

int print_tables_book(int tables_count)
{
	char string[50];
	int table_number;
	for (table_number = 0; table_number < tables_count; table_number++)
	{
		sprintf(string, "Table Number: %d\n", table_number + 1);
		drawline(string);
		print_table(table_number);
	}
}

int print_table(int table_number)
{
	int table_counter, product;
	for (table_counter = 0; table_counter < 10; table_counter++)
	{
		product = (table_number + 1) * (table_counter + 1);
		printf("%d X %d = %d\n", (table_number + 1), table_counter + 1, product);
	}
}