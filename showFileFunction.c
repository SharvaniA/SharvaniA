//function to show file.

int show_name()
{
	FILE * fp_show_file;
	char name_line[MAX_LENGTH];
	system("CLS");
	fp_show_file = fopen(FILE_NAME, "r");
	if(fp_show_file == NULL)
	{
		printf("Error!");
		exit(1);
	}
	while(fgets(name_line, sizeof(name_line), fp_show_file) != NULL)
	{
		printf("%s", name_line);
	}	
	fclose(fp_show_file);
	return 0;
}