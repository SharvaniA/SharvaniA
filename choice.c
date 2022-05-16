//Read save, print and exit program on file.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#define MAX_LENGTH 100
#define FILE_NAME "Names.dat"
#include "saveFileFunction.c"
#include "showFileFunction.c"
#include "removeNewlineFunction.c"
#include "menuFunction.c"
int main()
{
	int menu_option;
	menu();
}