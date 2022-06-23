//larger number program using functions concept.

#include <stdio.h>
#include "functionLarger.c"
int main()
{
	int number1, number2, check;
	printf("Enter two numbers to find larger between them: ");
	scanf("%d %d", &number1, &number2);
	check = checkLarger(number1, number2);
	if(check == 0)
	{
		printf("%d is equal to %d.\n", number1, number2);
	}
	else
	{
		printf("%d is larger than %d.\n", number1, number2);
	}
}
