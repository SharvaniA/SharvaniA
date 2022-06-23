#define NEWARRAY(T, N) ((T*) (malloc((N) * sizeof(T))))
char* perm(const char* s)
{
	char* result = NEWARRAY(char, strlen(s) + 1);
	strcpy(result, s);
	return result;
}