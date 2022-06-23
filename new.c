#include <stdio.h>
#include <string.h>
#include "showBytes.c"

int main() {
    
    char string1[100];
    int length;
    show_bytes(string1);
    length = strlen(string1);
    printf("length = %d", length);
    
    return 0;
}
