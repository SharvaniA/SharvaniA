int makeNull(char *string)
{
	string[strlen(string) - (strlen(string) - 1)] = '\0';
}