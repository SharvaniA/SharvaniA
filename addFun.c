// Adding two numbers. Unit testable function.

#include <stdio.h>
#include "functionAdd.c"
int main()
{
	int total;
	total = addNumbers(67, 99);
	printf("The sum of given two numbers is %d\n", total);
	total = addNumbers(-4, -9);
	printf("The sum of given two numbers is %d\n", total);
	total = addNumbers(0, 0);
	printf("The sum of given two numbers is %d\n", total);
	total = addNumbers(0, 89);
	printf("The sum of given two numbers is %d\n", total);
	total = addNumbers(0, -56);
	printf("The sum of given two numbers is %d\n", total);
	total = addNumbers(99, 99);
	printf("The sum of given two numbers is %d\n", total);
}
