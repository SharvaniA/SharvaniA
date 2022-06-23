// Printing n natural numbers.

#include <stdio.h>
#include <stdlib.h>
void displayNaturalNumbers(int number)
{
	if (number)
	{
		displayNaturalNumbers(number - 1);
	}
	else
	{
		return;
	}
	printf("%d\n", number);
}
int main()
{
	int limitOfNaturalNumber;
	printf("How many natural numbers do yo want to print?\n");
	scanf("%d", &limitOfNaturalNumber);
	printf("Natural Numbers:\n");
	displayNaturalNumbers(limitOfNaturalNumber);
}

