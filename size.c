#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
	int *intPtr;
	char *charPtr;
	printf("%d\n", sizeof(char*));
	printf("%d\n", sizeof(int*));
	printf("%d\n", sizeof(char));
	printf("%d\n", sizeof(int));
	printf("%d\n", sizeof(*charPtr));
	printf("%d\n", sizeof(*intPtr));
}