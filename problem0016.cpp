/*
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
*/

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>

#include "bigint/BigIntegerLibrary.hh"

using namespace std;

int main ()
{
    const int POWER = 1000;

    BigInteger x(1);
    for( int i = 0; i < POWER; i++ )
        x *= 2;

    BigInteger digit_sum(0);

    while( x > 0 )
    {
        digit_sum += x % 10;
        x /= 10;
    }

    cout << digit_sum << endl;

    return 0;
}

// EOF
