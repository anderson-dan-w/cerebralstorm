#include <stdio.h>
#define TOP 1000

#define NUM_DIVISORS 2
int divisors[NUM_DIVISORS] = {3, 5};


int main(void) {
    int total = 0;
    for (int i=0; i<TOP; i++) {
        for (int j=0; j<NUM_DIVISORS; j++) {
            int divisor = divisors[j];
            if (i % divisor == 0) {
                total += i;
                break;
            }
        }
    }
    printf("total: %d\n", total);
    return 0;
}
