//function for tables book using positive and negative table.

int runningTables(int countOfTables)
{
	int number, counter, product, originalNumber;
	char mySign;
	if(countOfTables < 0)
	{
		originalNumber = countOfTables;
		countOfTables = countOfTables * (-1);
	}
	for(number = 0; number <= countOfTables; number++)
	{
		printf("Table Number: %d\n", number);
		for(counter = 1; counter <= 10; counter++)
		{
			product = number * counter;
			mySign = originalNumber < 0 ? '-' : ' ';
			printf("%c%2d X %2d = %c%3d\n", mySign, number, counter, mySign, product);
		}
	}
}