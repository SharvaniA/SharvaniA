// function for series 1, 4, 27, 256...

#include <stdio.h>
int seriesRun(int series_count)
{
	int counter, term_counter, power;
	if(series_count < 0)
	{
		printf("Enter a valid number.");
	}
	else
	{
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
}
