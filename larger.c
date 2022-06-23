// Reading two numbers and finding out the larger between them.

#include <stdio.h>
int main()
{
	int number1, number2;
	printf("Enter two numbers to find larger between them: ");
	scanf("%d %d", &number1, &number2);
	if(number1 == number2)
	{
		printf("%d id equal to %d.\n", number1, number2);
	}
	else{
		if(number1 > number2)
		{
			number1;
			number2;
		}
		else
		{
			number1 = number1 + number2;
			number2 = number1 - number2;
			number1 = number1 - number2;
		}
		printf("%d is larger than %d.\n", number1, number2);
	    }
}