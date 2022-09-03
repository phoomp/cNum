#include <stdio.h>

#include "graph.h"

// Returns the index of the decimal place if the string is a valid number
// Else, returns -1
int typeCheckStringToNum(char* number, int numDigits) {
    bool decimalFound = false;
    int decimal = 0;

    for (int i = 0; i < numDigits; i++) {
        int num = (int)number[i];
        
        if (num >= 48 && num <= 57) continue;
        else if (i == 0 && num == 45) continue;
        else if (num == 46 && !decimalFound) {
            if (i == 0) {
                printf("Shorthand notations are not allowed.");
                return -1;
            }
            decimalFound = true;
            decimal = i;
        }
        else return -1;
    }

    return decimal;
}