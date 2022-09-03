#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

uint64_t factorial(uint64_t n) {
    uint64_t sum = n;
    
    for (n = n - 1; n > 0; n--) {
        sum *= n;
    }

    return sum;
}


// nCr = n! / r! (n - r)!

uint64_t combination(int n, int r) {
    if (r == 0 || n == r) return (uint64_t) 1;
    uint64_t nFac = factorial(n);
    uint64_t rFac = factorial(r);
    uint64_t n_rFac = factorial(n - r);

    return (uint64_t)(nFac / (rFac * n_rFac));
}

int main() {
    int aCo, bCo, aPow, bPow, n;

    printf("A coefficient: ");
    scanf("%d", &aCo);
    printf("\n");

    printf("A Power: ");
    scanf("%d", &aPow);
    printf("\n");

    printf("B coefficient: ");
    scanf("%d", &bCo);
    printf("\n");

    printf("B power: ");
    scanf("%d", &bPow);
    printf("\n");

    printf("N degree: ");
    scanf("%d", &n);
    printf("\n");

    // nth degree polynomial has n + 1 terms
    int* polynomial = (int*) malloc(sizeof(int) * (n + 1));
    
    for (int i=0; i<n + 1; i++) {
        // printf("%d", i);s
        uint64_t pascal = combination(n, i);
        uint64_t a = pow(aCo, (aPow * (n - i)));
        uint64_t b = pow(bCo, (bPow * i));

        // printf("%llu\n", pascal);

        polynomial[i] = pascal * a * b;
    }

    for (int i=0; i<n + 1; i++) {
        printf("%d\n", polynomial[i]);
    }
    
    return 0;
}