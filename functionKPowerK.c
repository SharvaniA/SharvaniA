//Funtion for k power k.

#include <stdio.h>
int calculationOfKpowerK(int base)
{
	int counter, product = 1;
	if(base < 0)
	{
		product = 0;
	}
	else 
	{
		if(base == 0)
		{
			printf("Inderminant\n");
		}
		else
		{
			for(counter = 1; counter <= base; counter++)
			{
				product = product * base;
			}
		}
	}
	return(product);
}