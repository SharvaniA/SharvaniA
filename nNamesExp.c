//Reading and Printing n Names with pointers 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGTH 30
int main()
{
	int names_count, names_counter;
	printf("How many names do you want to print? ");
	scanf("%d", &names_count);
	fflush(stdin);
	char **names;
	names = malloc(names_count * sizeof(char * ));
	for(names_counter = 0; names_counter < names_count; names_counter++)
	{
		names[names_counter] = malloc(MAX_LENGTH);
	}
	for(names_counter = 0; names_counter < names_count; names_counter++)
	{
		printf("Enter names %d of %d: ", names_counter + 1, names_count);
		fgets(names[names_counter], MAX_LENGTH, stdin);
	}
	for(names_counter = 0; names_counter < names_count; names_counter++)
	{
		remove_newline(names[names_counter]);
		printf("Names %d of %d: %s\n", names_counter + 1, names_count, names[names_counter]);
	}
}
int remove_newline(char * name)
{
	name[strlen(name) - 1] = '\0';
}