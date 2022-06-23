// function for Tables Book.

#include "functionSingleTable.c"
int runningTables(int countOfTables)
{
	int number;
	if(countOfTables < 1)
	{
		for(number = 0; number >= countOfTables; number--)
		{
			printTable(number);
		}
	}
	else
	{
		for(number = 1; number <= countOfTables; number++)
		{
			printTable(number);
		}
	}
}