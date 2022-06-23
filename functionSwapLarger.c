//function for swapping two numbers.

void swapIfNeededToHaveLargerFirst(int *number1, int *number2)
{
	if(*number1 < *number2)
	{
		*number1 = *number1 + *number2;
		*number2 = *number1 - *number2;
		*number1 = *number1 - *number2;
	}
}