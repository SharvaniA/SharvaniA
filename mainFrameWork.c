//CRUDS framework.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Tools.c"
#define MENU_FILE_NAME "menu.cfg"
#define FIELD_FILE_NAME "field.cfg"
#define DATA_FILE_NAME "framework.dat"
#define MAX_LENGTH 100
int linesCounter;
int linesCount;
char data[MAX_LENGTH];
char **fieldNames;
char **loadLines(char *fileName)
{
	FILE *fpLines;
	char line[100];
	char **lines;
	linesCounter = 0;
	fpLines = fopen(fileName, "r");
	while (fgets(line, sizeof(line), fpLines) != NULL)
	{
		linesCounter++;
	}
	linesCount = linesCounter;
	lines = malloc(linesCount * sizeof(char *));
	lines[0] = malloc(MAX_LENGTH);
	itoa(linesCount, lines[0], 10);
	rewind(fpLines);
	for (linesCounter = 1; linesCounter <= linesCount; linesCounter++)
	{
		lines[linesCounter] = malloc(MAX_LENGTH);
		fgets(lines[linesCounter], MAX_LENGTH, fpLines);
		remove_newline(lines[linesCounter]);
	}
	fclose(fpLines);
	return(lines);
}

int main()
{
	fieldNames = loadLines(FIELD_FILE_NAME);
	showMenu();
}

int showMenu()
{
	int option;
	char **menuLines;
	menuLines = loadLines(MENU_FILE_NAME);
	do
	{
		linesCount = atoi(menuLines[0]);
		for (linesCounter = 1; linesCounter <= linesCount; linesCounter++)
		{
			printf("%s", menuLines[linesCounter]);
			if (linesCounter < linesCount)
			{
				printf("\n");
			}
		}
		scanf("%d", &option);
		switch (option)
		{
			case 1:
				createRecord();
				break;
			case 2:
				displayRecord();
				break;
			case 3:
				printf("Exit.\n");
				exit(0);
			default :
				printf("Incorrect option.\n");
		}
	} while (option != 3);
}

int createRecord()
{
	FILE *fpData;
	fpData = fopen(DATA_FILE_NAME, "a");
	if(fpData == NULL)
	{
		printf("Error in opening.\n");
		exit(0);
	}
	fflush(stdin);
	linesCount = atoi(fieldNames[0]);
	for (linesCounter = 1; linesCounter <= linesCount; linesCounter++)
	{
		printf("Enter %s: ", fieldNames[linesCounter]);
		fgets(data, MAX_LENGTH, stdin);
		fwrite(data, sizeof(data), 1, fpData);
	}
	fclose(fpData);
}

int displayRecord()
{
	int dataStatus = 0;
	FILE *fpData;
	fpData = fopen(DATA_FILE_NAME, "r");
	if (fpData == NULL)
	{
		printf("File not found.\n");
		exit(0);
	}
	fflush(stdin);
	linesCount = atoi(fieldNames[0]);
	for (linesCounter = 1; linesCounter <= linesCount; linesCounter++)
	{
		if (fread(data, sizeof(data), 1, fpData) == 1)
		{
			dataStatus == 1;
			printf("%s: %s", fieldNames[linesCounter], data);
		}
		else
		{
			break;
		}
		if (linesCounter == linesCount)
		{
			linesCounter = 0;
		}
	}
	if (dataStatus == 0)
	{
		printf("No Record found.\n");
	}
	fclose(fpData);
}