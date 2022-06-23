// User Prime program

#include <stdio.h>
#include <math.h>
#include "funtionPrime.c"
int main()
{
	int number, result, primeCheck;
	printf("Enter a number to check whether the given number is prime number or not: ");
	scanf("%d", &number);
	primeCheck = checkPrime(number);
	if(primeCheck == 1)
	{
		printf("%d is a prime number.\n", number);
	}
	else 
	{
		printf("%d is not a prime number.\n", number);
	}
}
