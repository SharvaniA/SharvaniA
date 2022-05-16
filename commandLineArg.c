 // Printing all command-line arguments. (comman-line arguments)

 #include <stdio.h>
int main(int argc, char const *argv[])
{
	int counter;
	for(counter = 0; counter < argc; counter++)
	{
		printf("argv[%2d]: %s\n", counter, argv[counter]);
		getch();
	}
	return 0;
}