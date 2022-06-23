// Printing whether the given number is prime or not.

#include <stdio.h>
#include <math.h>
int main()
{
	int number, result, primeCheck;
	primeCheck = checkPrime(-6);
	if(primeCheck == 1)
	{
		printf("Passed!\n");
	}
	else 
	{
		printf("Failed!\n");
	}
	primeCheck = checkPrime(8);
	if(primeCheck == 1)
	{
		printf("Passed!\n");
	}
	else 
	{
		printf("Failed!\n");
	}
	primeCheck = checkPrime(2);
	if(primeCheck == 1)
	{
		printf("Passed!\n");
	}
	else 
	{
		printf("Failed!\n");
	}
	primeCheck = checkPrime(25);
	if(primeCheck == 1)
	{
		printf("Passed!\n");
	}
	else 
	{
		printf("Failed!\n");
	}
	primeCheck = checkPrime(17);
	if(primeCheck == 1)
	{
		printf("Passed!\n");
	}
	else 
	{
		printf("Failed!\n");
	}
	
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