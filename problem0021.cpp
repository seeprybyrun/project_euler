/*
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
*/

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>

class DivisorFinder
{
    static std::vector<int> primesTable;
    static int tableLimit;
    std::vector<int> divisors;
public:
    DivisorFinder( int n=2 ) { if(n > tableLimit) extendPrimesTable(n); /* divisors = findDivisors(n); */ }
    std::vector<int> allDivisors() const {std::vector<int> v(divisors); return v;}

    static void extendPrimesTable(int n);     // updates primesTable to include all primes up to n
};
int DivisorFinder::tableLimit = 2;
std::vector<int> DivisorFinder::primesTable(1,2);    // one int with value 2

int sumOfProperDivisors(int n);

int main()
{
    const int MAX = 10000;

    DivisorFinder d1(10);
    DivisorFinder d2(100);
    DivisorFinder::extendPrimesTable(200);

//    int *isAmicable = new int[MAX+1];   // isAmicable will be an array of 0, -1, and +1
//    isAmicable[0] = -1;                 // -1 means that the number is NOT amicable
//    for( int i = 1; i <= MAX; ++i )     // +1 means that the number IS amicable
//        isAmicable[i] = 0;              //  0 means that it is not yet known whether the number is amicable
//
//    for( int i = 1; i <= MAX; ++i )
//    {
//        if( isAmicable[i] != 0 ) continue;
//
//        int s = sumOfProperDivisors(i);
//        if( isAmicable[s] != 0 )
//        {
//            // impossible for i to be amicable if s is either not amicable or is amicable w/ another num
//            isAmicable[i] = -1;
//            continue;
//        }
//
//        int s2 = sumOfProperDivisors(s);
//        if( s2 == i )
//        {
//            isAmicable[i] = 1;
//            isAmicable[s] = 1;
//        }
//        else
//        {
//            isAmicable[i] = -1; // i is definitely NOT amicable; can't say anything about whether s is amicable
//        }
//    }
//
//    int sumOfAmicableNums = 0;
//    for( int i = 1; i <= MAX; ++i )
//    {
//        if( isAmicable[i] == 1 ) sumOfAmicableNums += 1;
//    }
//
//    std::cout << sumOfAmicableNums << std::endl;
//
//    return 0;
//}
//
//int sumOfProperDivisors(int n)
//{
//    int sum = 0;
//    /* ... */
//    return sum;
}

// updates primesTable to include all primes up to n
void DivisorFinder::extendPrimesTable(int n)
{
    // implemented using sieve of Eratosthenes

    int k = DivisorFinder::primesTable.size();
    DivisorFinder::primesTable.resize( k+(n-DivisorFinder::tableLimit) );
    // initializes new cells of primesTable to be the ints from tableLimit+1 to n
    for( int i = k; i < DivisorFinder::primesTable.size(); ++i )
    {
        DivisorFinder::primesTable[i] = DivisorFinder::tableLimit + i-k+1;
    }

    const int N = floor(sqrt(n))+1;

    for( int i = 0; DivisorFinder::primesTable[i] < N; ++i )
    {
        for( int j = i+1; j < DivisorFinder::primesTable.size(); ++j )
        {
            if( DivisorFinder::primesTable[j] % DivisorFinder::primesTable[i] == 0 )
                DivisorFinder::primesTable[j] = 0;
        }
    }

    // drop all zeroed-out elements
    std::vector<int>::iterator it;
    int count = 0;
    for( it = DivisorFinder::primesTable.begin(); it != DivisorFinder::primesTable.end(); ++it )
    {
        if( *it == 0 )
        {
//            ++it;
            DivisorFinder::primesTable.erase(it);
            it = DivisorFinder::primesTable.begin()+count;
//            --it;
        }
        else ++count;
    }

    // debug code
    for( int i = 0; i < DivisorFinder::primesTable.size(); ++i )
        std::cout << DivisorFinder::primesTable[i] << std::endl;

}

// EOF
