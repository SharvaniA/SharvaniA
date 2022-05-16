// array increment by + 1.

#include <stdio.h>
#include <stdlib.h>
int main()
{
	int n, marks, marks_counters;
	printf("Enter number of subjects: ");
	scanf("%d", &n);
	for(marks_counters = 0; marks_counters < n; marks_counters++)
	{
		printf("marks of students %d of %d: ", marks_counters + 1, n);
		scanf("%d", (marks + marks_counters));
	}
	for(marks_counters = 0; marks_counters < n; marks_counters++)
	{
		printf("marks of students %d of %d: %d\n", marks_counters + 1, n, marks[marks_counters]);
	}
}