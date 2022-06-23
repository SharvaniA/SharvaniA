// Printing factorial of a number by using recursion.

#include <stdio.h>
#include <limits.h>
#include <time.h>
long int printFactorialNumber(int number)
{
	if (number >= 1)
	{
		return number * printFactorialNumber(number - 1);
	}
	else
	{
		return 1;
	}
}
int main()
{
	int number;
	double timeSpent = 0.0;
	clock_t startTime = clock();
	printf("Enter a number to know its factorial value: ");
	scanf("%d", &number);
	printf("Factorial of the number %d is %ld\n", number, printFactorialNumber(number));
	clock_t endTime = clock();
	timeSpent += (double)(endTime - startTime) / CLOCKS_PER_SEC;
	printf("Time taken by the program is %f seconds", timeSpent);
	return 0;
}
