// prime number program for Test cases using function call.

#include <stdio.h>
#include "funtionPrime.c"
int main()
{
	int primeCheck, number;
	primeCheck = checkPrime(number);
	printf((checkPrime(-6) == 0) ? ("Passed\n") : ("Failed\n"));
	printf((checkPrime(2) == 1) ? ("Passed\n") : ("Failed\n"));                      
	printf((checkPrime(18) == 0) ? ("Passed\n") : ("Failed\n"));
	printf((checkPrime(39) == 1) ? ("Passed\n") : ("Failed\n"));
	(checkPrime(13) == 1) ? (printf("Passed\n")) : (printf("Failed\n"));
}
