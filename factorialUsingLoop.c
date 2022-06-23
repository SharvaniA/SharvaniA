// Printing factorial value of a number using loop.

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>
#include <unistd.h>
#include <sys/resource.h>
long getMemoryUsage()
{
	struct rusage myUsage;

	getrusage(RUSAGE_SELF, &myUsage);
	return myUsage.ru_maxrss;
}

int main()
{
	int number, product = 1, counter;
	double timeSpent = 0.0;
	clock_t startTime = clock();
	printf("Enter a number to find its factoria value: ");
	scanf("%d", &number);
	for (counter =1; counter <= number; counter++)
	{
		product = product * counter;
	}
	printf("Factorial of the number is %d\n", product);
	clock_t endTime = clock();
	timeSpent += (double)(endTime - startTime) / CLOCKS_PER_SEC;
	printf("Time taken by the program is %f seconds", timeSpent);
	printf("Memory usage: %ld\n", getMemoryUsage());
}