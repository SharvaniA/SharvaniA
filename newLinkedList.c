#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LENGTH 30
#define FILE_NAME "linkedList.txt"

struct node
{
	char name[MAX_LENGTH];
	struct node *next;
};

// function to display linked list
void displayLinkedList(struct node *root)
{
    struct node *temp = root;
    printf("\nLinkedList: ");
    while(temp!=NULL)
    {
        printf("%d %s -> ",temp->val, temp->name);
        temp = temp->next;
    }
    printf("NULL\n\n");
}


// function to write linked list to a file
void writeLinkedList(node* head)
{    
	struct node* temp = head;

	FILE* fpNames;
	file = fopen (FILE_NAME, "a");
	while(temp!=NULL)
	{
		fwrite(temp, sizeof(struct node), 1, fpNames);
		temp = temp->next;
	}
	fclose(fpNames);
}

struct node* readLinkedList(char filename[]){
    
    struct node* temp = (struct node *)malloc(sizeof(struct node));;
    struct node* head; // points to the first node of the linked list in the file
    struct node* last; // points to the last node of the linked list in the file
    last = head = NULL;
    
    FILE* file;
    file = fopen (filename, "r");
    if (file == NULL)
    {
        fprintf(stderr, "\nCouldn't Open File'\n");
        exit (1);
    }
    
    // reading nodes from the file
    // nodes are read in the same order as they were stored
    // we are using the data stored in the file to create a new linked list
    while(fread(temp, sizeof(struct node), 1, file))
    {
        
        if(head==NULL)
        {
            head = last = (struct node *)malloc(sizeof(struct node));
        }
        else
        {
            last->next = (struct node *)malloc(sizeof(struct node));
            last = last->next;
        }
        last->val = temp->val;
        strcpy(last->name, temp->name);
        last->next = NULL;
        
    }
    
    fclose(file);
    
    return head;
    
}