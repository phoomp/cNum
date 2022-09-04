#define MAX_NUM_DIGITS 1000000

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#include "graph.h"
#include "errors.h"

void addObject(char* number, GraphObject* obj, int numObjects) {
    GraphObject newObj;
    int numDigits = strnlen(number, MAX_NUM_DIGITS);
    int decimal = typeCheckStringToNum(number, numDigits);
    int startIndex = getStartIndex(number, numDigits);
    bool negative = isNegative(number);

    numDigits -= negative;

    newObj.negative = negative;

    if (decimal == 0) {
        printDebug("Decimal point not found. Make sure you would like an integer");
        newObj.power = numDigits - 1;
    }
    else {
        printDebug("Decimal point found\n");
        numDigits--;
        newObj.numDigits = numDigits;
        newObj.power = decimal - 1 - newObj.negative;

        newObj.digits = (short*)malloc(sizeof(short) * (numDigits - startIndex));
        printf("Allocated space for %d numbers\n", numDigits - startIndex);

        bool afterDecimal = false;
        for (int i = startIndex; i < numDigits + 1; i++) {
            if (i == decimal) {
                afterDecimal = true;
                continue;
            }
            newObj.digits[i - afterDecimal] = (short)(number[i] - 48);
            printf("Adding %d to index %d\n", (short)(number[i] - 48), i - afterDecimal);
        }
    }

    // for (int i=0; i<newObj.numDigits; i++) {
    //     printf("%d", newObj.digits[i]);
    // }

    printf("\nnumDigits: %d\n", numDigits);
    printf("decimal: %d\n", decimal);
    printf("power: %llu\n", newObj.power);
    printf("startIndex: %d\n", startIndex);
    
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