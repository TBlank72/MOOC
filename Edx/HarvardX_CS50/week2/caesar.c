#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main (int argc, char* argv[])
{
    if (argc != 2)
    {
        printf("please enter a key\n");
        return 1;
    }
    
    // set key, k, = argv[1]
    //int k = (int) argv[1];
    int k = atoi(argv[1]) % 26;
    
    
    if (k == 0)
    {
        printf("Please try a different key\n");
        return 1;
    }
    
    // Get original string, p
    //printf("please enter a string of plain text\n");
    char* p = GetString();
    
    // Iterate over p
    for (int i = 0, len = strlen(p); i < len; i++)
    {
        // initialize string c with length of p
        char c[len];
        
        // is current char uppercase?
        if (isupper(p[i]))
        {
            c[i] = ((p[i] - 65 + k) % 26) + 65;
            printf("%c", c[i]);
        }
        // is current char lowercase?
        else if (islower(p[i]))
        {
            c[i] = ((p[i]) - 97 + k) % 26 + 97;
            printf("%c", c[i]);
        }
        else
        {
            printf("%c", p[i]);
        }
        
    }
    
    printf("\n");
    

    
    return 0;
}