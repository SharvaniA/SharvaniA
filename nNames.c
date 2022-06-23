//Read and print n names without pointers.

#include <stdio.h>
#include <math.h>
void main()
{
	int names_count;
	int name_counter;
	printf("How many names do you want to print? ");
	scanf("%d", &names_count);
	char names[names_count][5];
	for(name_counter = 0; name_counter < names_count; name_counter++)
	{
		printf("Name %d: ", name_counter + 1);
		scanf("%4s", &names[name_counter]);
	}
	printf("%d Names given are : \n", names_count);
	for(name_counter = 0; name_counter < names_count; name_counter++)
	{
		printf("Person %d: ", name_counter + 1);
		printf("%s\n", names[name_counter]);
	}
	printf("\n");
}