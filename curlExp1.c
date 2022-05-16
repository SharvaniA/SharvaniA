//Finding temperature of given city usng curl.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Tools.c"
int main()
{
	char cityName[100];
	char commandLine[600];
	char *partOfData;
	char data[900];
	printf("Enter City Name: ");
	fgets(cityName, 40, stdin);
	remove_newline(cityName);
	sprintf(commandLine, "curl -k -s \"https://api.openweathermap.org/data/2.5/weather?q=%s&appid=e6b7427f8bf97526adf2869093c7509c&units=metric\" >weather.txt", cityName);
	system(commandLine);

	FILE *fpCurlWeatherFile;

	fpCurlWeatherFile = fopen("weather.txt", "r");
	fgets(data, sizeof(data), fpCurlWeatherFile);
	// fwrite(data, 900, 1, fpCurlWeatherFile);
	// fclose(fpCurlWeatherFile);

	// fpCurlWeatherFile = fopen("weather.txt", "r");
	// fread(data, sizeof(data), 1, fpCurlWeatherFile);
	partOfData = strtok(data, ": ,");
	while(partOfData != NULL)
	{
		partOfData = strtok(NULL, ": ,");
		if (strstr(partOfData, "\"temp\"") != NULL)
		{
			printf("Temperature of %s is ", cityName);
			partOfData = strtok(NULL, ": ,");
			printf("%s.", partOfData);
			break;
		}
	}
	fclose(fpCurlWeatherFile);
}