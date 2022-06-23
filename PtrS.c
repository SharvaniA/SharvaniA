#include <stdio.h>
int main()
{
	int *p;
	int a;
	p = &a;
	printf("p = ");
	scanf("%d", p);
	printf("*p = %d\n", *p);
	printf("p = %d\n", p);
	printf("&a = %d\n", &a);
}