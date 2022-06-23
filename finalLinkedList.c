// Sorting using Linked List.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Tools.c"
#define MAX_LENGTH 30
#define FILE_NAME "linkedList.txt"
struct node
{
	char name[MAX_LENGTH];
	struct node *next;
};

FILE *fpNames;
struct node *ptrPrevious;
struct node *head;
struct node *ptrNew;

char nameToCreate[MAX_LENGTH];
char name[MAX_LENGTH];
char nameToSearch[MAX_LENGTH];

void loadList()
{
	fpNames = fopen(FILE_NAME, "r");
	ptrPrevious = head;
	head = NULL;
	while (fread(name, MAX_LENGTH, 1, fpNames) != 0)
	{
		ptrNew = (struct node*)malloc(sizeof(struct node));
		strcpy(ptrNew->name, name);
		if (head == NULL)
		{
			head = ptrPrevious = ptrNew;
		}
		ptrNew->next = NULL;
		ptrPrevious->next = ptrNew;
		ptrPrevious = ptrNew;
	}
	fclose(fpNames);
}

void saveList()
{
	fpNames = fopen(FILE_NAME, "w");
	ptrPrevious = head;
	while (ptrPrevious != NULL)
	{
		fwrite(ptrPrevious->name, MAX_LENGTH, 1, fpNames);
		ptrPrevious = ptrPrevious->next;
	}
	fclose(fpNames);
}

void createList()
{
	ptrPrevious = (struct node*)malloc(sizeof(struct node));
	fflush(stdin);
	printf("Enter the name: ");
	fgets(nameToCreate, MAX_LENGTH, stdin);
	remove_newline(nameToCreate);
	strcpy(ptrPrevious->name, nameToCreate);
	ptrPrevious->next = NULL;
	if (head == NULL)
	{
		head = ptrPrevious;
		return;
	}
	else
	{
		struct node *ptrHead = head;
		while (ptrHead->next)
		{
			ptrHead = ptrHead->next;
		}
		ptrHead->next = ptrPrevious;
	}
}

void displayList()
{
	int namesCounter = 0;
	ptrPrevious = head;
	while (ptrPrevious != NULL)
	{
		namesCounter++;
		printf("%s\n", ptrPrevious->name);
		ptrPrevious = ptrPrevious->next;
	}
}

void update()
{
	ptrPrevious = head;
	fflush(stdin);
	printf("Enter the name to update: ");
	fgets(nameToSearch, MAX_LENGTH, stdin);
	remove_newline(nameToSearch);
	while (ptrPrevious != NULL)
	{
		if (strcmp(ptrPrevious->name, nameToSearch) == 0)
		{
			printf("Enter a name to update: ");
			fgets(nameToCreate, MAX_LENGTH, stdin);
			remove_newline(nameToCreate);
			strcpy(ptrPrevious->name, nameToCreate);
			printf("The updated name is %s\n", ptrPrevious->name);
			break;
		}
		ptrPrevious = ptrPrevious->next;
	}
}

// void delete()
// {
// 	ptrPrevious = head;
// 	struct node *ptrCurrent = head;
// 	fflush(stdin);
// 	printf("Enter the name to search: ");
// 	fgets(nameToSearch, MAX_LENGTH, stdin);
// 	remove_newline(nameToSearch);
// 	while (ptrPrevious != NULL)
// 	{
// 		if (strcmp(ptrPrevious->name, nameToSearch) == 0)
// 		{
// 			if (ptrPrevious == head)
// 			{
// 				head = ptrPrevious->next;
// 				printf("The deleted element is %s\n", ptrPrevious->name);
// 				free(ptrPrevious);
// 				break;
// 			}
// 			else
// 			{
// 				ptrCurrent->next = ptrPrevious->next;
// 				printf("The deleted element is %s\n", ptrPrevious->name);
// 				free(ptrPrevious);
// 				break;	
// 			}
// 		}
// 		ptrCurrent = ptrPrevious;
// 		ptrPrevious = ptrPrevious->next;
// 	}
// }

void delete(struct node *entry)
{
	struct node **indirect;
	indirect = &head;
	while ((*indirect) != entry)
	{
		indirect = &(*indirect)->next;
	}
	*indirect = entry->next;
}

void nodeOfString()
{
	ptrPrevious = head;
	fflush(stdin);
	printf("Enter the name to search: ");
	fgets(nameToSearch, MAX_LENGTH, stdin);
	remove_newline(nameToSearch);
	while (ptrPrevious != NULL)
	{
		if (strcmp(ptrPrevious->name, nameToSearch) == 0)
		{
			delete(ptrPrevious);
			break;
		}
		ptrPrevious = ptrPrevious->next;
	}
}

void sortList()
{
	char ptrPreviousName[MAX_LENGTH];
	struct node *ptrPrevious1;
	ptrPrevious = head;
	while (ptrPrevious->next != NULL)
	{
		ptrPrevious1 = ptrPrevious->next;
		while (ptrPrevious1 != NULL)
		{
			if (strcmp(ptrPrevious->name, ptrPrevious1->name) > 0)
			{
				strcpy(ptrPreviousName, ptrPrevious1->name);
				strcpy(ptrPrevious1->name, ptrPrevious->name);
				strcpy(ptrPrevious->name, ptrPreviousName);
			}
			ptrPrevious1 = ptrPrevious1->next;	
		}
		ptrPrevious = ptrPrevious->next;
	}
}

int main()
{
	int option;
	loadList();
	do
	{
		printf("Select one of the option below:\n1. Create Names.\n2. Display Names.\n3. Update Name and Show Updated Name.\n4. Delete Name.\n5. Sort Names and Show.\n6. Exit.\nChoose one option: ");
		scanf("%d", &option);
		switch (option)
		{
			case 1:
				createList();
				saveList();
				break;
			case 2:
				displayList();
				break;
			case 3:
				update();
				saveList();
				displayList();
				break;
			case 4:
				nodeOfString();
				saveList();
				break;
			case 5:
				sortList();
				saveList();
				displayList();
				break;
			case 6:
				printf("Exit.\n");
				exit(0);
		} 
	} while (option != 6);
}

