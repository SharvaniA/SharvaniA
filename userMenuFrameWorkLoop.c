
#define FILENAME "menu.cfg"
#include "Tools.c"
#define MAX_LENGTH 30
int userShowMenu()
{
	char descriptionOfOptions[60];
	int confirmation;
	char descriptionToChooseOption[60];
	int optionCounter;
	char option[MAX_LENGTH];
	FILE *fpMenuDetails;
	fpMenuDetails = fopen(FILENAME, "w");
	printf("Description before options list: ");
	fgets(descriptionOfOptions, 60, stdin);
	remove_newline(descriptionOfOptions);
	optionCounter = 1;
	do
	{
		fflush(stdin);
		printf("Option %d: ", optionCounter);
		fgets(option, MAX_LENGTH, stdin);
		remove_newline(option);
		printf("Do you want to add another option?\n1. Yes.\n2. No.\nChoose (1 or 2): ");
		scanf("%d", &confirmation);
		optionCounter++;
	} while (confirmation != 2);
	fflush(stdin);
	printf("Description after options list: ");
	fgets(descriptionToChooseOption, 60, stdin);
	fclose(fpMenuDetails);
	return 0;
}