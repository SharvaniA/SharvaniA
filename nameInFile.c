// Read a name and save it into a file. (file)

#include <stdio.h>
#include <stdlib.h>
int main()
{
	int name_counter, name_count;
	printf("How many names do you want to printf? ");
	scanf("%d", &name_count);
	fflush(stdin);
	char name[30];
	FILE *file_pointer;
	file_pointer = fopen("Names", "a");
	if(file_pointer == NULL)
	{
		printf("Error!");
		exit(1);
	}
	for(name_counter = 0; name_counter < name_count; name_counter++)
	{
		printf("Enter Name %d of %d: ", name_counter + 1, name_count);
		scanf("%s", name);
		fprintf(file_pointer, "Name %d of %d: %s\n", name_counter + 1, name_count, name);
	}
	fclose(file_pointer);
	return 0;
}