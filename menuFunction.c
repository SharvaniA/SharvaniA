//Function for menu.

int menu()
{
	int menu_option;
	do
	{
		printf("Select one of the below option to proceed:\n1. Save name.\n2. Show names.\n3. Exit.\n");
		printf("Choose(1, 2 or 3): ");
		scanf("%d", &menu_option);
		fflush(stdin);
		switch(menu_option)
		{
			case 1:
				save_name();
				break;
			case 2:
				show_name();
				break;
			default:
				printf("Exit!");
				exit(1);
		}
	}
	while(menu_option != 3);
	return 0;
}