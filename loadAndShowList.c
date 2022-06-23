#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGTH 30
// #define FILE_NAME "linkedList.txt"
#include "Tools.c"
char nameToCreate[MAX_LENGTH];
char nameToSearch[MAX_LENGTH];
struct node
{
	char name[MAX_LENGTH];
	struct node *next;
};

struct node *temp;
struct node *head;

void loadList()
{
	char name[MAX_LENGTH];
	FILE *fpNames;
	fpNames = fopen(FILE_NAME, "r");
	struct node *new;
	head = NULL;
	while (fgets(name, sizeof(name), fpNames) != NULL)
	{
		new = (struct node *)malloc(sizeof(struct node));
		strcpy(new->name, name);
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

void showList()
{
	temp = head;
	while (temp != NULL)
	{
		printf("%s", temp->name);
		temp = temp->next;
	}
}

int main()
{
	loadList();
	showList();
}
