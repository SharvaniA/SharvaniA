//Printing Tables Book function with positive and negative. 

#include <stdio.h>
#include "functionPNTable.c"
int main()
{
	int tables_count;
	printf("How many tables do you want to print in a tables book? ");
	scanf("%d", &tables_count);
	printf("Tables Book\n");
	printf("Tables upto: %d\n", tables_count);
	runningTables(tables_count);
}
