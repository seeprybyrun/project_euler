/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

#include <iostream>
#include <vector>

using namespace std;

#include "primality.h"

int main ()
{
    const int MAX = 2000000;
    int* nums = new int[MAX-2];
    // initialize nums to have the integers from 2 to MAX-1 (inclusive)
    for(int i = 0; i < MAX-2; i++) {
           nums[i] = i+2;
//           cout << nums[i] << endl;
    }

    // implement a sieve of Eratosthenes --- only need to go up to sqrt(MAX)
    for( int i = 0; i < MAX-2; i++ )
    {
        // find the next nonzero entry of the nums array
        if( nums[i] == 0 ) continue;

        // no need to continue if nums[i] > sqrt(MAX-1)
        if( nums[i]*nums[i] > MAX-1 ) break;

        // zero out any elements in nums which are divisible by nums[i]
        for( int j = i+1; j < MAX-2; j++ )
        {
            if( nums[j] % nums[i] == 0 ) nums[j] = 0;
        }
    }

//    for(int i = 0; i < MAX-2; i++) {
//           cout << nums[i] << endl;
//    }

    uint64_t sum = 0;
    for(int i = 0; i < MAX-2; i++)
        sum += nums[i];

    cout << sum << endl;

    delete[] nums;

    return 0;
}


// EOF
