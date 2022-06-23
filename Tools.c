//Function for underlining.

int drawline(char *string)
{
	int counter;
	int length = printf("%s", string);
	for (counter = 0; counter < length; counter++)
	{
		printf("_");
	}
	printf("\n");
}

//Function for remove new line.

int remove_newline(char *name)
{
	name[strlen(name) - 1] = '\0';
}

//Function for underling with space.

int under_line(char *name)
{
	int letter_counter, letters = 0, words = 1;
	for(letter_counter = 0; name[letter_counter] != '\0'; letter_counter++)
	{
		if(name[letter_counter] != ' ')
		{
			printf("-");
			letters++;
		}
		else if(name[letter_counter] == ' ')
		{
			printf(" ");
			words++;
		}
	}
}

//Function for underlining multiplication table.

int underline_table(int length)
{
	int counter;
	for (counter = 0; counter < length - 1; counter++)
	{
		printf("-");
	}
}

//Function for show bytes.

int show_bytes(char *name)
{
	int letters_counter;
	for(letters_counter = 0; letters_counter <= (strlen(name)); letters_counter++)
	{
		printf("letter %c: value %d\n", name[letters_counter], name[letters_counter]);
	}
}
