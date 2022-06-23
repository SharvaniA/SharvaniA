//Function to save file.

int save_name()
{
	int yes_no;
	char name[MAX_LENGTH];
	FILE * fp_save_name;
	fp_save_name = fopen(FILE_NAME, "a");
	if(fp_save_name == NULL)
	{
		printf("Error!");
		exit(1);
	}
	do
	{
		printf("Enter Name: ");
		fgets(name, sizeof(name), stdin);
		remove_newline(name);
		printf("Do you want to continue?\n1. Yes.\n2. No.\nChoose(1 or 2): ");
		scanf("%d", &yes_no);
		fflush(stdin);
		fprintf(fp_save_name, "Names: %s\n", name);
	}
	while(yes_no == 1);
	fclose(fp_save_name);
	return 0;
}