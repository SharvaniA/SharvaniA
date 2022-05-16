// Printing whether the given number is prime or not using Test Cases.

#include <stdio.h>
#include <math.h>
int main()
{
	int primeCheck, number;
	primeCheck = checkPrime(number);
	(checkPrime(-6) == 0) ? (printf("Passed\n")) : (printf("Failed\n"));
	(checkPrime(2) == 1) ? (printf("Passed\n")) : (printf("Failed\n"));                      
	(checkPrime(18) == 0) ? (printf("Passed\n")) : (printf("Failed\n"));
	(checkPrime(39) == 1) ? (printf("Passed\n")) : (printf("Failed\n"));
	(checkPrime(13) == 1) ? (printf("Passed\n")) : (printf("Failed\n"));
}
int checkPrime(int number)
{
	int rootNumber, primeCheck = 0, divisor;
	if(number <= 1 )
	{
		primeCheck = 0;
	}
	else if(number == 2)
	{
		primeCheck = 1;
	}
	else
	{
		if(number % 2 == 0)
		{
			primeCheck = 0;
		}
		else
		{
			rootNumber = sqrt(number);
			for(divisor = 1; divisor <= rootNumber; divisor+=2)
			{
				if(number % divisor == 0)
				{
					primeCheck = 0;
					break;
				}
			}
			primeCheck = 1;
		}
	}
	return(primeCheck);
}
