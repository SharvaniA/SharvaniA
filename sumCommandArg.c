//Printing sum of all command-line arguents.

#include <stdio.h>
#include <stdlib.h>
int main(int argument_char, char const *argument_variable[])
{
	int sum = 0, arguments_counter;
	if(argument_char < 1)
	{
		printf("\n Enter appropriate number of arguments to calculate sum. \n\n");
		exit(0);
	}
	else
	{
		for(arguments_counter = 0; arguments_counter < argument_char; arguments_counter++)
		{
			sum = sum + atoi(argument_variable[arguments_counter]);
		}
	}
	printf("\n Sum of all command-line arguments is %d \n\n", sum-1);
}