/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
*/

#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <sstream>

using namespace std;

#include "primality.h"

int main ()
{
    int MAX = 10001;
    int i = 4;
    int count = 2; // starting assuming 2 and 3 are counted already

    while( count < MAX ){
        while( i%6 != 1 && i%6 != 5 ) ++i; // only check for primality if i = +- 1 mod 6
        if( isPrime(i) ){
            ++count;
        }
        ++i; // increment i after testing for primality
    }

    cout << i-1;

    return 0;
}

// EOF
