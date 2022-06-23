//Overwriting names Experiment

#include <stdio.h>
#include <string.h>

int main()
{
	int names_counter;
	char names[3][2];
	for(names_counter = 0; names_counter < 3; names_counter++)
	{
		printf("Names %d of %d: ", names_counter + 1, 3);
		scanf("%s", names[names_counter]);
	}
	for(names_counter = 0; names_counter < 3; names_counter++)
	{
		printf("Names %d of %d: %s\n", names_counter + 1, 3, names[names_counter]);
	}
} 