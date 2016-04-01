#include <stdio.h>
#include <cs50.h>

// 1 min = 192 ounces
// 192 ounces = 12, 16 ounce bottles of water
int main(void)
{
    int b;
    
    printf("How many minutes do you shower? \n");
    
    b = GetInt() * 12;
    
    printf("You use %d bottles of water each time you shower\n", b);
}