//malloc pointer++ and + 1.

#include <stdio.h>
#include <stdlib.h>
int main()
{
	int *Ptrmarks, *PtrStart, subject_count, marks_counter;
	printf("Enter number of subjects: ");
	scanf("%d", &subject_count);
	Ptrmarks = malloc(subject_count * sizeof(int));
	PtrStart = Ptrmarks;
	for(marks_counter = 0; marks_counter < subject_count; marks_counter++)
	{
		printf("Enter the marks of subject %d of %d: ", marks_counter + 1, subject_count);
		scanf("%d", Ptrmarks);
		Ptrmarks++;
	}
	Ptrmarks = PtrStart;
	for(marks_counter = 0; marks_counter < subject_count; marks_counter++)
	{
		printf("Subject %d of %d: %d\n", marks_counter + 1, subject_count, *Ptrmarks);
		Ptrmarks++;
	}
}