/*
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/

#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
using namespace std;

int main () {

    const int MAX = 100;

    // sum of squares
    int sumOfSquares = MAX*(MAX+1)*(2*MAX+1)/6;

    // square of sum
    int squareOfSum = MAX*MAX*(MAX+1)*(MAX+1)/4;

    cout << squareOfSum-sumOfSquares;

    return 0;
}

// EOF
