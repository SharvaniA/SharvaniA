// Read and print 5 marks. (array)

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main() 
{
  int subjects_count;
  int marks_counter;
  printf("\n\n How many subject marks do you want to print? \n");
  scanf("%d", &subjects_count);
  int values[subjects_count];
  for(marks_counter = 0; marks_counter < subjects_count; marks_counter++) 
  {
    printf("\nSubject %d : ", marks_counter + 1);
    scanf("%d", &values[marks_counter]);
  }
  printf("Displaying marks obtained:\n");
  for(marks_counter = 0; marks_counter < subjects_count; marks_counter++)
  {
     printf("Subject %d : %d\n", marks_counter + 1, values[marks_counter]);
  }
}