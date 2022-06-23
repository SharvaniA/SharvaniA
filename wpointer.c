//N number with pointers.

#include <stdio.h>
#define MAX_SIZE 100
int main()
{
    int array[MAX_SIZE];
    int subjects_count, counter;
    int *ptr;
    ptr = array;
    printf("Enter number of subjects: ");
    scanf("%d", &subjects_count);
    printf("Enter marks:\n");
    for (counter = 0; counter < subjects_count; counter++)
    {
        scanf("%d", (ptr + subjects_count);   
    }
    printf("Marks List: ");
    for (counter = 0; counter < subjects_count; counter++)
    {
        printf("%d", *(ptr + subjects_count));
    }
    return 0;
}