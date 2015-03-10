/*
Starting in the top left corner of a 2×2 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20×20 grid?
*/

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

uint64_t product(int low, int high);
uint64_t binom(int n, int k);

int main ()
{
    const int GRID_SIZE = 20;

    cout << binom(2*GRID_SIZE,GRID_SIZE) << endl;

    return 0;
}

//uint64_t product(int low, int high)
//{
//    uint64_t prod = 1;
//    for( int i = low; i <= high; i++ )
//        prod *= i;
//    return prod;
//}

uint64_t binom(int n, int k)
{
    int *denom_factors = new int[n-k+1];
    denom_factors[0] = 0;
    denom_factors[1] = 0;
    for( int i = 2; i <= n-k; i++ )
        denom_factors[i] = 1;

    uint64_t prod = 1;
    for( int i = n; i >= k+1; i-- )
    {
        prod *= i;
        for( int j = n-k; j >= 2; j-- )
        {
            // searches for the largest integer in the denominator (not already used)
            //   to cancel with the numerator --- this takes more time, but it helps
            //   evade the overflow issue which occurs by computing the numerator first,
            //   then the denominator, then dividing the two
            if( denom_factors[j] > 0 && prod % j == 0 )
            {
                prod /= j;
                denom_factors[j] = 0;
            }
        }
    }

    delete[] denom_factors;

    return prod;
}

// EOF
