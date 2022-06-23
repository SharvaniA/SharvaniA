//Print given name given number of times. (command_ line arguments)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int arguments_count, char const *arguments_variable[])
{
	int counter, times;
	printf("How many time do you what to print the given argument? ");
	scanf("%d", &times);
	for(counter = 0; counter < times; counter++)
	{
		printf("%s\n", arguments_variable[1]);
	}
	return 0;
}