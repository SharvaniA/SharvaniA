#include <stdio.h>
#include <stdlib.h>
int main()
{
	int count;
	printf("Enter the value of count: ");
	scanf("%d", &count);
	int marks[count];
	marks[0] = 98;
	marks[1] = 97;
	marks[2] = 100;
	printf("address = %d\n", &marks[count]);
	printf("%d\n", marks[0]);
	printf("%d\n", &marks[0]);
	printf("%d\n", marks[1]);
	printf("%d\n", &marks[1]);
	printf("%d\n", marks[2]);
	printf("%d\n", &marks[2]);
}