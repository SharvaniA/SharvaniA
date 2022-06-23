//Reading names and printing then with uderline.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "removeNewlineFunction.c"
#define MAX_LENGTH 30
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
		printf("Names: ");
		fgets(names + MAX_LENGTH * names_counter, MAX_LENGTH, stdin);
		remove_newline(names + MAX_LENGTH * names_counter);
	}
	for(names_counter = 0; names_counter < names_count; names_counter++)
	{
		underline_string(names + MAX_LENGTH * names_counter);
		printf("\n");
	}
}

int underline_string(char *string)
{
	int length = printf("%s", string);
	int counter;
	printf("\n");
	for (counter = 0; counter < length; counter++)
	{
		printf("-");
	}
}