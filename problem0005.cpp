/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
using namespace std;

int largestPower(int n, int p);

int main () {

    const int NUMPRIMES = 8;
    const int MAX = 20;

    const int PRIMES[NUMPRIMES] = {2,3,5,7,11,13,17,19};
    int largestNumberFactors[NUMPRIMES] = {0,0,0,0,0,0,0,0};

    int lcm = 1;

    for( int i = 0; i < NUMPRIMES; i++ ) {
        // counts largest number of factors of current prime present among all the integers from 1 to MAX
        int largestNumberFactors = 0;
        for( int j = 0; j < MAX; j++ ){
            largestNumberFactors = max(largestNumberFactors,largestPower(j+1,PRIMES[i]));
        }
        // multiplies lcm by the correct power of the current prime
        lcm *= pow(PRIMES[i],largestNumberFactors);
    }

    cout << "LCM of integers 1 to " << MAX << ": " << lcm << endl;

    return 0;
}

int largestPower(int n, int p) {

    // finds the largest power of p which divides n evenly
    int count = 0;
    while( n % p == 0 ) {
        count += 1;
        n /= p;
    }
    return count;
}

// EOF
