#include <stdlib.h>
#include <stdbool.h>

typedef __uint64_t uint64_t;

typedef struct GraphObject {
    char* name;
    uint64_t leastPrecision;
    uint64_t leastSignificant;

    // If undefined, we do not evaluate this object at all.
    bool undefined;

    // Numbers are always stored as fraction for the highest precision.
    bool negative;
    uint64_t numNumerators;
    uint64_t numDenominators;
    unsigned short* numerators;
    unsigned short* denominators;
    uint64_t numPower;
    uint64_t denomPower;

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
int getStartIndex(char* number, int numDigits);
bool isNegative(char* number);