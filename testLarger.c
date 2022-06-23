//larger number program using functions concept.

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "functionSwapLarger.c"
int main()
{
	int number1, number2;
	number1 = 89;
	number2 = 89;
	if(number1 == number2)
	{
		printf("%d is equal to %d.\n", number1, number2);
		exit(0);
	}
	swapIfNeededToHaveLargerFirst(&number1, &number2);
	printf("%d is larger than %d.\n", number1, number2);
	number1 = 99;
	number2 = 78;
	if(number1 == number2)
	{
		printf("%d is equal to %d.\n", number1, number2);
		exit(0);
	}
	swapIfNeededToHaveLargerFirst(&number1, &number2);
	printf("%d is larger than %d.\n", number1, number2);
	number1 = 67;
	number2 = 88;
	if(number1 == number2)
	{
		printf("%d is equal to %d.\n", number1, number2);
		exit(0);
	}
	swapIfNeededToHaveLargerFirst(&number1, &number2);
	printf("%d is larger than %d.\n", number1, number2);
	number1 = -33;
	number2 = -33;
	if(number1 == number2)
	{
		printf("%d is equal to %d.\n", number1, number2);
		exit(0);
	}
	swapIfNeededToHaveLargerFirst(&number1, &number2);
	printf("%d is larger than %d.\n", number1, number2);
	number1 = -67;
	number2 = -99;
	if(number1 == number2)
	{
		printf("%d is equal to %d.\n", number1, number2);
		exit(0);
	}
	swapIfNeededToHaveLargerFirst(&number1, &number2);
	printf("%d is larger than %d.\n", number1, number2);
	number1 = -77;
	number2 = -33;
	if(number1 == number2)
	{
		printf("%d is equal to %d.\n", number1, number2);
		exit(0);
	}
	swapIfNeededToHaveLargerFirst(&number1, &number2);
	printf("%d is larger than %d.\n", number1, number2);
	number1 = 0;
	number2 = 34;
	if(number1 == number2)
	{
		printf("%d is equal to %d.\n", number1, number2);
		exit(0);
	}
	swapIfNeededToHaveLargerFirst(&number1, &number2);
	printf("%d is larger than %d.\n", number1, number2);
	number1 = 0;
	number2 = 2;
	if(number1 == number2)
	{
		printf("%d is equal to %d.\n", number1, number2);
		exit(0);
	}
	swapIfNeededToHaveLargerFirst(&number1, &number2);
	printf("%d is larger than %d.\n", number1, number2);
}
