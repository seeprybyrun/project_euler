/*
n! means n*(n-1)*...*3*2*1

For example, 10! = 10*9*...*3*2*1 = 3628800,
and the sum of the digits in the number 10! is 3+6+2+8+8+0+0 = 27.

Find the sum of the digits in the number 100!
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
    BigInteger fact = 1;
    int sum = 0;

    for( int i = 2; i <= 100; ++i )
    {
        fact *= i;
 //       cerr << fact << endl;
        while( fact % 10 == 0 ) fact /= 10;
    }

    while( fact > 0 )
    {
        BigInteger t = fact%10;
        sum += t.toInt();
        fact /= 10;
    }

    cout << sum << endl;

    return 0;
}

// EOF
