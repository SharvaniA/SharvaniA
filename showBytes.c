int show_bytes(char *name)
{
	int letters_counter;
	for(letters_counter = 0; letters_counter <= (strlen(name)); letters_counter++)
	{
		printf("letter %c: value %d\n", name[letters_counter], name[letters_counter]);
	}
}