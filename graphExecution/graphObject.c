#define MAX_NUM_DIGITS 1000000

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#include "graph.h"
#include "errors.h"

void addObject(char* number, GraphObject* obj, int numObjects) {
    GraphObject newObj;
    
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