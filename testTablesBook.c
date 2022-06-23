//Printing Tables Book function. 

#include <stdio.h>
#include "functionTables.c"
int main()
{
	printf("Tables Book\n");
	printf("Tables upto: 5");
	runningTables(5);
	printf("Tables upto: 0");
	runningTables(0);
	printf("Tables upto: -2");
	runningTables(-2);
}
