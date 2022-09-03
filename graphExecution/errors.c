#include "errors.h"

void printDebug(char* message) {
    printf("NOTE: %s\n", message);
    return;
}

void raiseWarning(char* message) { 
    printf("WARNING: %s\n", message);
    return;
}

void raiseNonCriticalError(char* message) {
    printf("NON-CRITICAL ERROR: %s\n", message);
    return;
}

void raiseCriticalErrorAndExit(int exitCode, char* message) {
    printf("ERROR: %s\n", message);
    printf("Exiting with %d...\n", exitCode);
    exit(exitCode);
    return;
}