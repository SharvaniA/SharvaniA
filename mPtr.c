#include <stdio.h>
#include <stdlib.h>
int main()
{
	int *marks;
	int count;
	printf("Enter count value: ");
	scanf("%d", &count);
	marks = malloc(count * sizeof(int));
	marks[0] = 80;
	marks[1] = 99;
	printf("marks address = %u\n", marks);
	printf("marks = %d\n", *marks);
	marks++;
	printf("marks address = %u\n", marks);
	printf("marks = %d\n", *marks);
}