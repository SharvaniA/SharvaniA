//Index.

#include <stdio.h>
#include <stdlib.h>
int main()
{
	int *ptrMarks, subjectCount, marksCounter;
	printf("Enter number of subjects: ");
	scanf("%d", &subjectCount);
	ptrMarks = malloc(subjectCount * sizeof(int));
	for(marksCounter = 0; marksCounter < subjectCount; marksCounter++)
	{
		printf("Marks of students %d of %d: ", marksCounter + 1, subjectCount);
		scanf("%d", &ptrMarks[marksCounter]);
	}
	for(marksCounter = 0; marksCounter < subjectCount; marksCounter++)
	{
		printf("Marks of students %d of %d: %d\n", marksCounter + 1, subjectCount, ptrMarks[marksCounter]);

	}
}