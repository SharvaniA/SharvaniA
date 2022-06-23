// printing series [10, 22, 46, 94, 190...]

#include <stdio.h>
int main()
{
	int termCount, counter, number;
	printf("How many numbers do you want to print in a series of number given 10, 22, 46, 94, 190...? ");
	scanf("%d", &termCount);
	printf("The first %d terms of the series are: ", termCount);
	number = 10;
	if(termCount == 1)
	{
		printf("10.\n");
	}
	if(termCount < 1)
	{
	}
	else
	{
		printf("10, ");
		for(counter = 2; counter <= termCount; counter++)
		{
			number = number * 2;
			number = number + 2;
			printf("%d", number);
			if(counter < termCount)
			{
				printf(", ");
			}
		}
		if(termCount >= 0)
		{
			printf(".");
		}
	}
}