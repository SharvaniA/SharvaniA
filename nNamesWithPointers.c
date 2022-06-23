//Read and print n Names with pointers.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGTH 100
int main()
{
	int names_count, name_counter;  
	printf("Enter number of names: ");
	scanf("%d", &names_count);
	fflush(stdin);
	char **names;
	names = malloc(names_count * sizeof(char *));
	for(name_counter = 0; name_counter < names_count; name_counter++)
	{
		names[name_counter] = malloc(MAX_LENGTH);
	}
	for(name_counter = 0; name_counter < names_count; name_counter++)
	{
		printf("Enter name %d of %d: ", name_counter + 1, names_count);
		fgets(names[name_counter], MAX_LENGTH, stdin);
	}
	for(name_counter = 0; name_counter < names_count; name_counter++)
	{
		printf("Names %d of %d: %s", name_counter + 1, names_count, names[name_counter]);
	}
}