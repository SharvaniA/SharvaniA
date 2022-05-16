// Array without pointer

#include <stdio.h>
#include <stdlib.h>
#define SUBJECT_COUNT 5
int main()
{
	int marks[SUBJECT_COUNT], marks_counter;
	for(marks_counter = 0; marks_counter < SUBJECT_COUNT; marks_counter++)
	{
		printf("Enter marks of the students %d of %d: ", marks_counter + 1, SUBJECT_COUNT);
		scanf("%d", (&marks[marks_counter]));
	}
	for(marks_counter = 0; marks_counter < SUBJECT_COUNT; marks_counter++)
	{
		printf("Marks of the students %d of %d: %d\n", marks_counter + 1, SUBJECT_COUNT, marks[marks_counter]);
	}
}