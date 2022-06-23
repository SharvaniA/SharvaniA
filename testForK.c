//Printing k power k.

#include <stdio.h>
#include "functionKPowerK.c"
int main()
{
	int product;
	product = calculationOfKpowerK(9);
	printf("The value of k power k is %d.\n", product);
	product = calculationOfKpowerK(0);
	printf("The value of k power k is %d.\n", product);
	product = calculationOfKpowerK(1);
	printf("The value of k power k is %d.\n", product);
	product = calculationOfKpowerK(-5);
	printf("The value of k power k is %d.\n", product);
}
