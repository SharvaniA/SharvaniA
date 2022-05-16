//Reading and printing n Names code with one pointer.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGTH 20
int main()
{
	int names_counter, names_count;
	printf("How many names do you want to print? ");
	scanf("%d", &names_count);
	fflush(stdin);
	char *names;
	names = malloc(names_count * MAX_LENGTH);
	for(names_counter = 0; names_counter < names_count; names_counter++)
	{
		printf("Enter names %d of %d: ", names_counter + 1, names_count);
		fgets(names + MAX_LENGTH * names_counter, MAX_LENGTH, stdin);
	}
	for(names_counter = 0; names_counter < names_count; names_counter++)
	{
		printf("Names: %s", names + MAX_LENGTH * names_counter);
	}
}
