#include <stdio.h>
//#include "cs50.h"
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <locale.h>

// reference.cs50.net

// type def
typedef char* string;


void say(char word[15]);

int main(int argc, char* argv[])
{

  //string name;
  //printf("Enter your name: \n");
  //name = GetString();
  //printf("hello, %s\n", name);

  /*
  for (int i = 0; i < argc; i++)
  {
    printf("%s\n", argv[i]);
  }

  printf("argc = %i\n", argc);
  */


  /* -----ASCII example ------
  printf("%c\n", 65);
  printf("%d\n", 'a' - 'A');
  printf("%d\n", ('z' - 'a' + 1) % 26 + 'a');
  printf("%d\n", 'b' + 'z');
  */





  /* ----- ASCII chars -----
  for (int i = 0; i < 127; i++)
  {
    printf("%i is %c\n", i, (char) i);
  }
  */
  
  /* ----type def test -----*/

  string name = "Todd";
  printf("%s\n", name); 



}//end main


void say(char word[15])
{
    printf("%s\n", word);
}
