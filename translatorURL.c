// Dictionary Translator.

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "Tools.c"
#define MAX_LENGTH 30
// #define FILE_NAME "translatorURL.txt"
int main()
{
	char wordToSearch[MAX_LENGTH];
	char commandLine[200];
	char data[4000];
	char *partOfData;
	// char *dataResult;

	printf("Enter a word to translate into Telugu: ");
	fgets(wordToSearch, MAX_LENGTH, stdin);
	remove_newline(wordToSearch);
	fflush(stdin);
	sprintf(commandLine, "curl -k \"https://dict.hinkhoj.com/shabdkhoj.php?word=%s&ie=UTF-8\" > translatorURL.dat", wordToSearch);
	system(commandLine);

	FILE *fpWordTranslator;
	fpWordTranslator = fopen("translatorURL.dat", "r");
	// fgets(data, sizeof(data), fpWordTranslator);
	// dataResult = strdup(data);
	// partOfData == strsep(data, "><=}{:.\"");
	while (fgets(data, sizeof(data), fpWordTranslator) != NULL)
	{
		// printf("1\n");
		partOfData = strtok(data, "><=");
		while (partOfData != NULL)
		{
			// printf("2\n");
			// printf("%s\n", partOfData);
			partOfData = strtok(NULL, "><=");
			// printf("%s\n", partOfData);
			if (partOfData != NULL)
			{
				// printf("3\n");
				// printf("%s\n", partOfData);
				//fgets(data, sizeof(data), fpWordTranslator);
				// partOfData = strtok(data, "><=");
				if (strcmp(partOfData, "\"https://dict.hinkhoj.com/hindi-words/listb.php\"") == 0)
				{
					printf("4\n");
			// 		printf("In Telugu: ");
					partOfData = strtok(NULL, "><=");
					printf("%s\n", partOfData);
					break;
				}
				// break;
			}
		}
	}
	fclose(fpWordTranslator);
}