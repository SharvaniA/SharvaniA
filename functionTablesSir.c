// function for Tables Book.

#include "functionSingleTable.c"
int runningTables(int countOfTables)
{
	int number;
	for((countOfTables < 1 ? number = 0 : number = 1); (countOfTables < 1 ? number >= countOfTables : number <= countOfTables); (countOfTables < 1 ? number– : number++))
{
	printTable(number);
}
}