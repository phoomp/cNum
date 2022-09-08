#include <stdio.h>
#include <string.h>

#include "graph.h"
#include "errors.h"

// Return true if the number, passed as char*, has "-" at index 0
bool isNegative(char* number) {
    int size = sizeof(number);

    if (size < sizeof(char)) {
        raiseCriticalErrorAndExit(-1, "Invalid pointer to number string");
    }

    if (number[0] == '-') {
        if (strnlen(number, 10) <= 1) {
            raiseCriticalErrorAndExit(-1, "Invalid number format");
        }
        printDebug("Negative number");
        return true;
    }
    else {
        printDebug("Positive number");
        return false;
    }
}

// Looks for ONE (1) / sign only. More than one slash results in an error.
bool isFraction(char* number, long maxDigits) {
    long c = 0;
    
    for (long i = 0; i < maxDigits; i++) {
        if (number[i] == '/') {
            c++;
            if (c > 1) {
                raiseCriticalErrorAndExit(-1, "Found more than 1 '/'!");
            }
            else if (i == 0 || i == maxDigits - 1) {
                raiseCriticalErrorAndExit(-1, "Found / at the beginning or the end!");
            }
        }
    }
}

int getStartIndex(char* number, int numDigits) {
    int i;
    for (i = 0; i < numDigits; i++) {
        if ((i < numDigits - 1 && (number[i] != '0' && number[i] != '.')) && number[i] != '-') {
            break;
        }
    }
    return i;
}


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
            if (i == 0 || i == numDigits - 1) {
                raiseCriticalErrorAndExit(-1, "Shorthand notations are not allowed.");
            }
            decimalFound = true;
            decimal = i;
        }
        else {
            raiseCriticalErrorAndExit(-1, "Invalid number format");
        }
    }

    return decimal;
}