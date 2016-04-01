#include <stdio.h>
#include <cs50.h>

int main(void)
{
    printf("how high is mario's pyramid? \n Must be between 1 and 23\n");
    int ph = GetInt(); 
    if (ph == 0)
        return 0;
    while (ph < 1 || ph > 23)
    {
        printf("try again\n");
        ph = GetInt();
    }
    
    for (int i = 0; i < ph; i++)
    {
        
        for (int j = ph; j > i + 1; j--)
        {
            printf(" ");
        }
        for (int k = 0; k < i + 2; k++)
        {
            
            printf("#");
        }
        
        printf("\n");
    }
    
}