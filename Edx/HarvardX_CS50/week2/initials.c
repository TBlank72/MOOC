#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    
    // Get Name from user
    string name = GetString();
    
    // Loop through chars
    for (int i = 0, len = strlen(name); i < len; i++)
    {
        // print first char upper
        if (i == 0)
        {
            printf("%c", toupper(name[0]));
        }
        // if space, print next char upper
        if (name[i] == 32)
        {
            printf("%c", toupper(name[i+1]));
        }
        
    }
    printf("\n");
    return 0;
}