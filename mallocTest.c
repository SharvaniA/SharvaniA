//Incrementing using malloc.

#include <stdio.h>
#include <stdlib.h>
#define MAX_LENGTH 30
int main()
{
	int marks[5];
	int grades[MAX_LENGTH];
	int *pMarks;
	pMarks = malloc(5 * sizeof(int));
	printf("marks[0] = ");
	scanf("%d\n", pMarks);
	printf("marks[0] = %d\n", *pMarks);
	printf("address of marks[0] = %d\n", pMarks);
	pMarks++;
	printf("marks[1] = ");
	scanf("%d\n", pMarks);
	printf("marks[1] = %d\n", *pMarks);
	printf("address of marks[1] = %d\n", pMarks);
}