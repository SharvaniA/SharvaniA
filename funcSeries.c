// Series [1, 4, 27, 256...]

#include <stdio.h>
#include "functionSeries.c"
int main()
{
	printf("Series of the powers of the number are: ");
	seriesRun(4);
	printf("\nSeries of the powers of the number are: ");
	seriesRun(0);
	printf("\nSeries of the powers of the number are: ");
	seriesRun(1);
	printf("\nSeries of the powers of the number are: ");
	seriesRun(-3);
}