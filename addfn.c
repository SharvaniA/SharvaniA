// Adding two number.

#include <stdio.h>
int main()
{
	int number1, number2;
	printf("Enter two numbers to add: ");
	scanf("%d%d", &number1, &number2);
	printf("The summation of %d and %d is %2d.\n", number1, number2, addNumber(number1, number2));
}
int addNumber(int number1, int number2)
{
	return(number1 + number2);
}