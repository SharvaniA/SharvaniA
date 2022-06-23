// Printing n terms of the series [1, 4, 27, 256,...]

#include <stdio.h>
int main()
{
	int series_count, term_counter, counter, power;
	printf("How many numbers do you want to print in a series of powers of their number? ");
	scanf("%d", &series_count);
	printf("The first %d terms of the series of the powers of the number are: ", series_count);
	for(term_counter = 1; term_counter <= series_count; term_counter++)
	{
		power = 1;
		for(counter = 1; counter <= term_counter; counter++)
		{
			power = power * term_counter;
		}
		printf("%d", power);
		if(term_counter < series_count)
			{
				printf(", ");
			}		
	}
	if(term_counter > series_count)
		{
			printf(".");
		}
}