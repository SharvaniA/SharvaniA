// function for prime numbers.

#include <stdio.h>
#include <math.h>
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
