//Sorting names.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Tools.c"
#define FILE_NAME "names.txt"
#define MAX_LENGTH 40
FILE *fpNames;
char name[MAX_LENGTH];
char newNames[MAX_LENGTH];
struct allStudentNames
{
	char name[MAX_LENGTH];
	struct allStudentNames *nextPtr;
};

struct allStudentNames *firstPtr;

void createLinkedList(int numberOfNodes);

void sortLinkedList(int numberOfNodes);

void displayLinkedList();

int main()
{
	showMenu();
}

void createLinkedList(int numberOfNodes)
{
	struct allStudentsNames *newNode;
	struct allStudentsNames *currentNode;
	int nodeData;
	int nodeCtr;

	firstNode = (struct allStudentsNames*)malloc(sizeof(struct allStudentsNames));

	fpNames = fopen(FILE_NAME, "r");
	fread()

}

int showMenu()
{
	int option;
	do
	{
		printf("Select one option to proceed.\n1. Save Names.\n2. Show Names.\n3. Sort and Show Names Alphabetically.\n4. Sort and Save Names Alphabetically.\n5. Exit.\nChoose one: ");
		scanf("%d", &option);
		switch (option)
		{
			case 1:
				saveNames();
				break;
			case 2:
				showNames();
				break;
			case 3:
				sortAndShowAlphabetically();
				break;
			case 4:
				sortAndSaveAlphabetically();
				break;
			case 5:
				printf("Exit.\n");
				break;
			default:
				exit(0);
		}
	} while (option != 5);
}

int saveNames()
{
	int confirmation;
	fpNames = fopen(FILE_NAME, "a");
	if (fpNames == NULL)
	{
		printf("Error in opening file.\n");
		exit(0);
	}
	struct allStudentNames studentNames;
	do
	{
		fflush(stdin);
		printf("Enter Name: ");
		fgets(studentNames.name, MAX_LENGTH, stdin);
		remove_newline(studentNames.name);
		fwrite(studentNames.name, sizeof(studentNames), 1, fpNames);
		printf("Do you want to continue?\n1. Yes.\n2. No.\nChoose one: ");
		scanf("%d", &confirmation);
	} while (confirmation != 2);
	fclose(fpNames);
	return 0;
}

int showNames()
{
	int namesCounter = 1;
	fpNames = fopen(FILE_NAME, "r");
	if (fpNames == NULL)
	{
		printf("Error in opening file.\n");
		exit(0);
	}
	struct allStudentNames studentNames;
	while (fread(studentNames.name, sizeof(studentNames), 1, fpNames) != 0)
	{
		printf("Name %d: %s\n", namesCounter, studentNames.name);
		namesCounter++;
	}
	fclose(fpNames);
	return 0;
}

int sortAndShowAlphabetically()
{
	
	return 0;
	fclose(fpNames);
}

int sortAndSaveAlphabetically()
{
	return 0;
}