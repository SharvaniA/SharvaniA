//Function for larger number program.

int checkLarger(int number1, int number2)
{
	int check;
	if(number1 == number2)
	{
		return 0;
	}
	else 
	{
		if(number1 > number2)
		{
			number1;
			number2;
		}
		else
		{
			number1 = number1 + number2;
			number2 = number1 - number2;
			number1 = number1 - number2;
		}
		return 1;
	}
}
