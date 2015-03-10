/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
a^2+b^2=c^2.
For example, 3^2+4^2=9+16=25=5^2.

There exists exactly one Pythagorean triple for which a+b+c=1000.
Find the product abc.
*/

#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <sstream>
using namespace std;

int main ()
{
    const int MAX = 1000;

    for( int a = 1; a < MAX; a++ )
    {
        for( int b = a+1; a+b < MAX; b++ )
        {
            int c = MAX-a-b;
            if( a*a + b*b != c*c ) continue;
            else cout << a << "*" << b << "*" << c << "=" << a*b*c << endl;
        }
    }

    return 0;
}


// EOF
