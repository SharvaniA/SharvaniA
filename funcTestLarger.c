//larger number program using functions concept.

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "functionSwapLarger.c"
int main()
{
	int number1, number2;
	printf("Enter two numbers to find larger number between them: ");
	scanf("%d%d", &number1, &number2);
	if(number1 == number2)
	{
		printf("%d is equal to %d.\n", number1, number2);
		exit(0);
	}
	swappingForLarger(&number1, &number2);
	printf("%d is larger than %d.\n", number1, number2);
}
