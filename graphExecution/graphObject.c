#define MAX_NUM_DIGITS 1000000

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#include "graph.h"

void addObject(char* number, GraphObject* obj, int numObjects) {
    GraphObject newObj;
    int numDigits = strnlen(number, MAX_NUM_DIGITS);

    int decimal = typeCheckStringToNum(number, numDigits);

    if (decimal == -1) {
        printf("Invalid number.. Exiting\n");
        exit(-1);
    }
    else if (decimal == 0) {
        printf("No decimal values\n");
    }
    else {
        printf("Found decimal: %d\n", decimal);

        // We don't count a decimal point as a digit
        numDigits--;
    }

    // Deal with negative numbers
    int startIndex = 0;
    if (number[0] == '-') {
        newObj.negative = true;

        // Make sure we don't count the extra "-"
        numDigits--;
        startIndex++;
    } 
    else {
        newObj.negative = false;
    }
        
    // Get rid of extra 0s in front
    while (startIndex < numDigits && (number[startIndex] == '0')) {
        startIndex++;
    }
    if (number[startIndex] == '.') {
        startIndex++;
    }

    // Instantiate the object's value
    newObj.numDigits = (numDigits - startIndex);
    
    newObj.digits = (short*)malloc(sizeof(short) * newObj.numDigits);

    // Decimal == 0 means the number is an integer
    if (decimal == 0) {
        newObj.power = numDigits - 1;
    }
    else {
        newObj.power = numDigits - decimal + 1;

        bool foundDecimal = false;

        for (int i = 0; i < newObj.numDigits; i++) {
            if (i == decimal) {
                foundDecimal = true;
            }
            printf("Adding digit: %d\n", (number[startIndex + i + foundDecimal] - 48));
            newObj.digits[i] = (short)(number[startIndex + i + foundDecimal] - 48);
        }
    }

    printf("Start idx: %d\n", startIndex);
    printf("newObj.power: %llu\n", newObj.power);
    printf("newObj.numDigits: %llu\n", newObj.numDigits);

    for (int i=0; i<newObj.numDigits; i++) {
        if (i == newObj.power - 1) printf("%c", '.');
        printf("%d", newObj.digits[i]);
    }

    printf("\npower: %llu\n", newObj.power);
    return;
}

Graph CreateGraph() {
    Graph newGraph;
    newGraph.addObject = &addObject;
    return newGraph;
}

int main() {
    Graph graph = CreateGraph();

    char number[MAX_NUM_DIGITS];
    
    printf("Input a number: ");
    scanf("%s", number);

    // graph.addObject("-3", graph.objects, graph.numObjects);
    graph.addObject(number, graph.objects, graph.numObjects);

    return 0;
}