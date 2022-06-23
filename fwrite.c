//Printing Alphabets.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
	char asciiValue[4] = "ABCD";
	int *ptrAlphabets;
	ptrAlphabets = (int*)asciiValue;
	printf("%d\n", *ptrAlphabets);
}