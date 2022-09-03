#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void printDebug(char* message);
void raiseWarning(char* message);
void raiseNonCriticalError(char* message);
void raiseCriticalErrorAndExit(int exitCode, char* message);