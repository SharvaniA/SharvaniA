//Printing k power k.

#include <stdio.h>
int main()
{
	int base, product = 1, counter;
	printf("Enter the value of k to print k to the power of k: ");
	scanf("%d", &base);
	for(counter = 1; counter <= base; counter++)
	{
		product = product * base;
	}
	printf("The value of %d power %d value is %d.\n", base, base, product);
}