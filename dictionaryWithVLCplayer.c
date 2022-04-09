//Use a dictionary api to show the meaning of a given name and also play the pronunciation.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Tools.c"
int main()
{
	
	
	
	
	char wordToSearch[20];
	char urlCommandLine[200];
	char vlcCommandLine[200];
	char data[1000];
	char *partOfData;
	printf("Enter word to search: ");
	fgets(wordToSearch, 20, stdin);
	remove_newline(wordToSearch);
	sprintf(urlCommandLine, "curl -k -s \"https://api.dictionaryapi.dev/api/v2/entries/en/%s\" > meaning.dat\n", wordToSearch);
	system(urlCommandLine);

	FILE *fpCurlDicFile;

	fpCurlDicFile = fopen("meaning.dat", "r");
	fgets(data, sizeof(data), fpCurlDicFile);
	partOfData = strtok(data, ":[],{};");
	while (partOfData != NULL)
	{
		partOfData = strtok(NULL, ":[],{};");
		if(strstr(partOfData, "\"definition\"") != NULL)
		{
			printf("Definition: ");
			partOfData = strtok(NULL, ":[],{};");
			printf("%s\n", partOfData);
			break;
		}
		else if(strstr(partOfData, "\"audio\"") != NULL)
		{
			partOfData = strtok(NULL, "[],{}");
			sprintf(vlcCommandLine, "vlc %s\n", partOfData);
			system(vlcCommandLine);
		}
	}
	fclose(fpCurlDicFile);
}
