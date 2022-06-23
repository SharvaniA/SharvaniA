#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node
{
	int data;
	struct node *nextPtr;
};

struct node *firstNode;

void createLinkedList(int numberOfNodes);

void sortLinkedList(int numberOfNodes);

void displayLinkedList();

int main()
{
	int numberOfNodes;

	firstNode = NULL;

	printf("numberOfNodes: ");
	scanf("%d", &numberOfNodes);

	createLinkedList(numberOfNodes);
	sortLinkedList(numberOfNodes);

	printf("Sorted:\n");
	displayLinkedList();
	return 0;
}

void createLinkedList(int numberOfNodes)
{
	struct node *newNode;
	struct node *currentNode;
	int nodeData;
	int nodeCtr;

	firstNode = (struct node *)malloc(sizeof(struct node));

	if (firstNode == NULL)
	{
		printf("Menry can not be allocated.");
	}
	else
	{
		printf("Input the elements in the linked list: ");
		scanf("%d", &nodeData);

		firstNode->data = nodeData;

		firstNode->nextPtr = NULL;

		currentNode = firstNode;

		for (nodeCtr = 2; nodeCtr <= numberOfNodes; nodeCtr++)
		{
			newNode = (struct node*)malloc(sizeof(struct node));
			if (newNode == NULL)
			{
				printf("Memory can not be allocated.");
			}
			else
			{
				scanf("%d", &nodeData);

				newNode->data = nodeData;

				newNode->nextPtr = NULL;

				currentNode->nextPtr = newNode;

				currentNode = currentNode->nextPtr;
			}
		}
	}
}

void sortLinkedList(int numberOfNodes)
{
	int nodeCtr;
	int ctr;
	int nodeDataCopy;
	struct node *currentNode;
	struct node *nextNode;

	for (nodeCtr = numberOfNodes -2; nodeCtr >= 0; nodeCtr--)
	{
		currentNode = firstNode;
		nextNode = currentNode->nextPtr;

		for (ctr = 0; ctr <= nodeCtr; ctr++)
		{
			if (currentNode->data > nextNode->data)
			{
				nodeDataCopy = currentNode->data;
				currentNode->data = nextNode->data;
				nextNode->data = nodeDataCopy;
			}

			currentNode = nextNode;
			nextNode = nextNode->nextPtr;
		}
	}
}
void displayLinkedList()
{
	struct node *currentNode;

	currentNode = firstNode;

	while (currentNode != NULL)
	{
		printf("%d\t", currentNode->data);

		currentNode = currentNode->nextPtr;
	}
}