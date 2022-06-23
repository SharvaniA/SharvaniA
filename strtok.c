//Read a sentence and print all the words in it one below the other, using strtok() function.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
	char sentence[100];
	char *partsOfSentence;
	printf("Enter a sentence: ");
	fgets(sentence, 100, stdin);
	partsOfSentence = strtok(sentence, " ");
	while (sentence != NULL)
	{
		printf("%s\n", partsOfSentence);
		partsOfSentence = strtok(NULL, " ");
	}
}