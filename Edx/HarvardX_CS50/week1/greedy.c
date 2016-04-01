#include <stdio.h>
#include <math.h>
#include <cs50.h>

int main(void)
{
    float change = 0.00;
    int changeR = 0;
    int coins = 0;
    
    do
    {
        printf("How much change is owed? \n");
        change = GetFloat();
        
    }
    while (change <= 0);
    changeR = round(change * 100);
    
    while (changeR >= 25)
    {
        changeR -= 25;
        coins++;
    }
    while (changeR >= 10 && changeR < 25)
    {
        changeR -= 10;
        coins++;
    }
    while (changeR >= 5 && changeR < 10)
    {
        changeR -= 5;
        coins++;
    }
    while(changeR > 0 && changeR < 5)
    {
        changeR -= 1;
        coins++;
    }
    
    printf("%i\n", coins);
    
    return 0;
}