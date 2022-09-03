#include <stdlib.h>
#include <stdbool.h>

typedef struct GraphObject {
    char* name;
    uint64_t leastPrecision;
    uint64_t leastSignificant;

    bool negative;
    uint64_t numDigits;
    short* digits;
    uint64_t power;

} GraphObject;

typedef struct GraphOperation {
    char* name;
    char* methodName;
    int type;
    int method;
    
} GraphOperation;

typedef struct Graph {
    char* name;
    int numObjects;
    GraphObject* objects;

    int numOperations;
    GraphOperation* operations;

    // Graph Functions
    void (*addObject)(char* number, GraphObject* objects, int numObjects);

} Graph;


// graphObject.c
Graph CreateGraph();
void addObject(char* number, GraphObject* obj, int numObjects);

// typeCheck.c
int typeCheckStringToNum(char* number, int numDigits);
bool isNegative(char* number);