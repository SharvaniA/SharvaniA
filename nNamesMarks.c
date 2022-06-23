//Reading and Prining names of students withtheir total marks.


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGTH 20
#define MARKS_LENGTH 100
int main()
{
	int names_counter, names_count, subject_count, marks_counter, sum = 0;
	printf("How many names do you want to print? ");
	scanf("%d", &names_count);
	fflush(stdin);
	printf("How many subject marks do you want to enter? ");
	scanf("%d", &subject_count);
	fflush(stdin);
	int marks[MARKS_LENGTH];
	int *ptrMarks;
	ptrMarks = marks;
	char *names;
	names = malloc(names_count * MAX_LENGTH);
	for(names_counter = 0; names_counter < names_count; names_counter++)
	{
		printf("Enter student name %d of %d: ", names_counter + 1, names_count);
		fgets(names + MAX_LENGTH * names_counter, MAX_LENGTH, stdin);
		sum = 0;
		remove_newline(names + MAX_LENGTH * names_counter);
		for(marks_counter = 0; marks_counter < subject_count; marks_counter++)
		{
			printf("Enter marks of subject %d of %d of %s: ", marks_counter + 1, subject_count, names + MAX_LENGTH * names_counter);
			scanf("%d", (ptrMarks + subject_count));
			sum = sum + *(ptrMarks + subject_count);
		}
		printf("Total marks = %d\n", sum);
		fflush(stdin);
	}
	for(names_counter = 0; names_counter < names_count; names_counter++)
	{
		printf("Total marks of %s is %d\n", names + MAX_LENGTH * names_counter, sum);
	}
}
int remove_newline(char * name)
{
	name[strlen(name) - 1] = '\0';
}

