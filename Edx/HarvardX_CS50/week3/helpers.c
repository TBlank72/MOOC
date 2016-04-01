/**
 * helpers.c
 *
 * Computer Science 50
 * Problem Set 3
 *
 * Helper functions for Problem Set 3.
 */
       
#include <cs50.h>
#include <stdio.h>
#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    // if n !positive return false
    if (n < 1)
    {
        return false;
    }
    
    // binary search beginning
    int final = n - 1;
    int first = 0;
    
    while (final >= first)
    {
        int mid = (final + first) / 2;
        if (values[mid] == value)
        {
            return true;
        }
        else if (values[mid] > value)
        {
            final = mid - 1;
        }
        else
        {
            first = mid + 1;
        }
    } // binary search ending
    
    /* linear search
    for (int i = 0; i < n; i++)
    {
        if (value == values[i])
        {
            return true;
        }
        else
        {
            continue;
        }
    }*/
    
    return false;
    
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    // bubble sort values[] from smallest to largest
    bool cont;
    do
    {
        cont = false;
        for (int i = 0; i < n - 1; i++)
        {
            if (values[i + 1] < values[i])
            {
                int a = values[i];
                values[i] = values[i + 1];
                values[i + 1] = a;
                cont = true;
            }
            
        } 
    } while (cont);
   
    
    return;
}