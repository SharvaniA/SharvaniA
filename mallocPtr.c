//Using malloc with pointers.

#include <stdio.h>
#include <stdlib.h>
int main()
{
	int count, *intptr;
	char *charptr;
	printf("Enter count value: ");
	scanf("%d", &count);
	intptr = malloc(count * sizeof(int));
	charptr = malloc(count * sizeof(char));
	printf("Enter value of intptr: ");
	scanf("%d", intptr);
	printf("Enter value of charptr: ");
	scanf("%s", charptr);
	printf("*intptr = %d\n", *intptr);
	printf("*charptr = %c\n", *charptr);
	printf("intptr = %u\n", intptr);
	printf("charptr = %u\n", charptr);
	intptr++;
	charptr++;
	printf("intptr++ = %u\n", intptr);
	printf("charptr++ = %u\n", charptr);
}