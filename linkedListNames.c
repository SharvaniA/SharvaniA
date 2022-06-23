#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGTH 30
#define FILE_NAME "linkedList.txt"
#include "Tools.c"
char nameToCreate[MAX_LENGTH];
char nameToSearch[MAX_LENGTH];
struct node
{
	char name[MAX_LENGTH];
	struct node *next;
};

struct node *head;
struct node *temp;
FILE *fpNames;

void saveList();
void displayFromList();
void update();
void delete();
void sortlistAndShow();
// void saveToFile();
// void openFile();

char name[MAX_LENGTH];

void loadList()
{
	fpNames = fopen(FILE_NAME, "r");
	struct node *new;
	temp = head;
	head = NULL;
	while (fgets(name, sizeof(name), fpNames) != NULL)
	{
		new = (struct node *)malloc(sizeof(struct node));
		strcpy(new->name, name);
		printf("%s\n", new->name);
		if(head == NULL)
		{
			head = temp = new;
		}
		new->next = NULL;
		temp->next = new;
		temp = new;
	}
	fclose(fpNames);
}


void saveList()
{
	fpNames = fopen(FILE_NAME, "w");
	temp = head;
	while (temp != NULL)
	{
		printf("1\n");
		fwrite(temp, sizeof(temp), 1, fpNames);
		temp = temp->next;
	}
	fclose(fpNames);
}

void sortlistAndShow()
{
	struct node *temp = head;
	struct node *new = temp->next;
	char tempName[MAX_LENGTH];
	while (temp != NULL)
	{
		if (strstr(temp->name, new->name) > 0)
		{
			strcpy(tempName, new->name);
			strcpy(new->name, temp->name);
			strcpy(temp->name, tempName);
		}
		temp = temp->next;
		saveList();
	}
	temp = head;
	while (temp != NULL)
	{
		printf("%s\n", temp->name);
		temp = temp->next;
	}
}

void createList()
{
	struct node *temp = (struct node*)malloc(sizeof(struct node));
	fflush(stdin);
	printf("Enter the name: ");
	fgets(nameToCreate, MAX_LENGTH, stdin);
	strcpy(temp->name, nameToCreate);
	temp->next = NULL;
	if(head == NULL) 
	{
		head = temp;
		return;
	}
	else
	{
		struct node *headPtr = head;
		while ((headPtr->next) != NULL)
		{
			headPtr = headPtr->next;
		}
		headPtr->next = temp;
	}
	saveList();
}

int main()
{
	int option;
	//head = NULL;
	do
	{
		loadList();
		printf("Select any one of the options mentioned below2:\n1. Save Names in to file.\n2. Display Names.\n3. Update Name.\n4. Sort and Show Names.\n5. Delete Name.\n6. Sort and Save Names to file.\n7. Display Sorted and Saved Names.\n8. Exit.\nChoose option: ");
		scanf("%d", &option);
		switch (option)
		{
			case 1:
				createList();
				break;
			case 2:
				displayFromList();
				break;
			case 3:
				update();
				break;
			case 4:
				delete();
				break;
			case 5:
				sortlistAndShow();
				break;
			// case 6:
			// 	saveToFile();
			// 	break;
			// case 7:
			// 	openFile();
			// 	break;
			case 6:
				printf("Exit.\n");
				exit(0);
		} 
	} while (option != 6);
}


void displayFromList()
{
	struct node *temp = head;
	int namesCounter = 0;
	while (temp != NULL)
	{
		namesCounter++;
		printf("%d: %s\n", namesCounter, temp->name);
		temp = temp->next;
	}
}


void update()
{
	struct node *temp = head;
	// struct node *temp1 = head;
	fflush(stdin);
	printf("Enter the name to search: ");
	fgets(nameToSearch, MAX_LENGTH, stdin);
	while (temp != NULL)
	{
		if(strcmp(temp->name, nameToSearch) == 1)
		{
			// temp1 = temp1->next;
			// struct node *temp2 = temp1->next;
			// temp1->next = temp2->next;
			printf("Enter a name to update: ");
			fgets(nameToCreate, MAX_LENGTH, stdin);
			strcpy(temp->name, nameToCreate);
			printf("The updated element is %s\n", temp->name);
			// writeListAndSave(nameToCreate);
			saveList();
		}
		temp = temp->next;
	}
	fclose(fpNames);
}

void delete()
{
	struct node *temp = head;
	struct node *temp1 = head;
	fflush(stdin);
	printf("Enter the name: ");
	fgets(nameToSearch, MAX_LENGTH, stdin);
	while ((fread(temp, sizeof(temp), 1, fpNames)) != 0)
	{
		if(strcmp(temp1->name, nameToSearch) == 1)
		{
			temp1 = temp1->next;
			struct node *temp2 = temp1->next;
			temp1->next = temp2->next;
			saveList();
			printf("The deleted element is %s\n", temp2->name);
			free(temp2);
			// writeListAndSave(nameToCreate);
		}
	}
}

void sortList()
{
	char tempName[MAX_LENGTH];
	temp = head;
	head = (struct node*)malloc(sizeof(struct node));
	while (new != NULL)
	{
		new = temp->next;
		if (strcmp(temp->name, new->name) > 0)
		{
			strcpy(tempName, new->name);
			strcpy(new->name, temp->name);
			strcpy(temp->name, tempName);
		}
		temp = temp->next;
	}
}

void showSortedList()
{
	int namesCounter = 0;
	temp = head;
	while (temp != NULL)
	{
		namesCounter++;
		printf("%s\n", temp->name);
		temp = temp->next;
	}
}

// void sortlist()
// {
// 	char tempName[MAX_LENGTH];
// 	struct node *temp = head;
// 	struct node *temp1 = temp->next;
// 	while (fread(temp, sizeof(temp), 1, fpNames) != 0)
// 	{
// 		if(strcmp(temp->name, temp1->name) > 0)
// 		{
// 			strcpy(tempName, temp1->name);
// 			strcpy(temp1->name, temp->name);
// 			strcpy(temp->name, tempName);
// 			// writeListAndSave(nameToCreate);
// 		}
// 		temp = temp->next;
// 	}
	// while ((fread((head), sizeof(head), 1, fpNames)) != 0)
	// {
	// 	printf("%s\n", temp->name);
	// }
// }


// void saveToFile()
// {
// 	FILE *fpNames;
// 	fpNames = fopen(FILE_NAME, "a");
// 	struct node *temp = head;
// 	int namesCounter = 0;
// 	while (temp != NULL)
// 	{
// 		namesCounter++;
// 		// writeListAndSave(nameToCreate);
// 		temp = temp->next;
// 	}
// 	fclose(fpNames);
// }

// void openFile()
// {
// 	FILE *fpNames;
// 	fpNames = fopen(FILE_NAME, "r");
// 	struct node *temp = head;
// 	while(fread(head, sizeof(head), 1, fpNames) != 0)
// 	{
// 		printf("%s\n", temp->name);
// 		temp = temp->next;
// 	}
// 	fclose(fpNames);
// }