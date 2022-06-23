//Experiment on underLining.

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
		printf("Names: ");
		fgets(names + MAX_LENGTH * names_counter, MAX_LENGTH, stdin);
	}
	for(names_counter = 0; names_counter < names_count; names_counter++)
	{
		printf("%s", names + MAX_LENGTH * names_counter);
		under_line(names + MAX_LENGTH * names_counter);
		printf("\n");
	}
}
int under_line(char *name)
{
	int letter_counter, letters = 0, words = 1;
	for(letter_counter = 0; name[letter_counter] != '\0'; letter_counter++)
	{
		if(name[letter_counter] != ' ')
		{
			printf("-");
			letters++;
		}
		else if(name[letter_counter] == ' ')
		{
			printf(" ");
			words++;
		}
	}
}