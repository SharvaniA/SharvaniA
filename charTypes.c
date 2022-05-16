// Program to explain different features writing a name or string.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGTH 30
int main()
{
	char name1[MAX_LENGTH];
	char name2[MAX_LENGTH];
	int counter;
	printf("Enter name2: ");
	scanf("%s", name2);
	fflush(stdin);
	printf("Enter name1: ");
	fgets(name1, MAX_LENGTH, stdin);
	printf("%s and %s are two names.\n", name1, name2);
	printf("After");
	for(counter = 0; counter < MAX_LENGTH; counter++)
	{
		printf("for name1 %c and %d\n", name1[counter], name1[counter]);
	}
	for(counter = 0; counter < MAX_LENGTH; counter++)
	{
		printf("for name2 %c and %d\n", name2[counter], name2[counter]);
	}
}