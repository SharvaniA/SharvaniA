//Experiment 2. 2D array.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "showBytes.c"
#define MAX_LENGTH 10
int main()
{
	int names_counter, names_count;
	printf("How many names do you want to print? ");
	scanf("%d", &names_count);
	fflush(stdin);
	char names[names_count][MAX_LENGTH];
	for(names_counter = 0; names_counter < names_count; names_counter++)
	{
		printf("Enter names %d of %d: ", names_counter + 1, names_count);
		fgets(names[names_counter], MAX_LENGTH, stdin);
	}
	for(names_counter = 0; names_counter < names_count; names_counter++)
	{
		printf("Names %d of %d: %s", names_counter + 1, names_count, names[names_counter]);
		show_bytes(names[names_counter]);
	}
}