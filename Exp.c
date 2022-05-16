#include <stdio.h>
int main()
{
int a = 10;
int b = 29;
int *c;
int **d;
int e;
int f;
printf("a = %d\n", a);
printf("b = %d\n", b);
printf("&a = %u\n", &a);
printf("&b = %u\n", &b);
printf("&a = %d\n", &a);
printf("&b = %d\n", &b);
printf("size of a = %d\n", sizeof(a));
printf("size of b = %d\n", sizeof(b));
printf("size of *c = %d\n", sizeof(*c));
printf("size of **d = %d\n", sizeof(**d));
printf("e = %d\n", e);
printf("f = %d\n", f);
}
