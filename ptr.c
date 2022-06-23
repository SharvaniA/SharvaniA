//Pointers

#include <stdio.h>
#include <stdlib.h>
int main()
{
	int *intPtr;
	char *charPtr;
	int number;
	char name[100];
	intPtr = &number;
	charPtr = name;
	printf("Enter intPtr: ");
	scanf("%d", intPtr);
	printf("Enter charPtr: ");
	scanf("%s", name);
	printf("intPtr: %d\n", *intPtr);
	printf("charPtr: %c\n", *charPtr);
	printf("address of intPtr: %u\n", intPtr);
	printf("address of charPtr: %u\n", charPtr);
}