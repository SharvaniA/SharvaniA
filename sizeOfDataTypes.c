//Checking the sizes of various data types and their variables.

#include <stdio.h>
int main()
{
	int marks[10];
	int grades[10];
	int salary;
	int *balance;
	char name[20];
	char *city;
	printf("size of marks[10]: %d\n", sizeof(marks));
	printf("size of grades[10]: %d\n", sizeof(grades));
	printf("size of salary: %d\n", sizeof(salary));
	printf("size of *balance: %d\n", sizeof(*balance));
	printf("size of name[20]: %d\n", sizeof(name));
	printf("size of *city: %d\n", sizeof(*city));
}