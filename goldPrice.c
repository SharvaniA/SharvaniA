//program to know gold price.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
	char currency[5];
	char commandLine[200];
	char data[600];
	char *partOfData;
	printf("Which to currency do you want to change USD: ");
	scanf("%s", currency);
	sprintf(commandLine, "curl -s -X GET -H \"X-API-KEY:2a8b4a9c349aed636dce6bdc68a6b66b2a8b4a9c\" \"http://goldpricez.com/api/rates/currency/%s/measure/all\" > goldFile.dat", currency);
	system(commandLine);

	FILE *fpGoldPrice;

	fpGoldPrice = fopen("goldFile.dat", "r");
	fgets(data, sizeof(data), fpGoldPrice);
	// fwrite(data, 600, 1, fpGoldPrice);
	// fclose(fpGoldPrice);

	// fpGoldPrice = fopen("goldFile.dat", "r");
	// fread(data, sizeof(data), 1, fpGoldPrice);
	partOfData = strtok(data, ",:\"");
	while (partOfData != NULL)
	{
		partOfData = strtok(NULL, ",:\"");
		if(strstr(partOfData, "gram_in_inr") != NULL)
		{
			printf("One gram of gold in rupees is ");
			partOfData = strtok(NULL, ",:\"");
			printf("%s Rupees.\n", partOfData);
			break;
		}
	}
	fclose(fpGoldPrice);
}