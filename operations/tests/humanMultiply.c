#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_NUM_DIGITS 1000

void solve(char* a, char* b, char* ans) {

}

int main() {
    while (1) {
        char* a = malloc(sizeof(char) * 10000);
        char* b = malloc(sizeof(char) * 10000);
        printf("Input a number: ");
        scanf("%s\n", &a);

        printf("Input another number: ");
        scanf("%s\n", b);

        printf("%s\n", a);
        char* ans = (char*) malloc(sizeof(char) * pow(MAX_NUM_DIGITS, 2));

        free(ans);
    }
    return 0;
}