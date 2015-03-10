/*
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

uint64_t collatz(uint64_t n);

int main ()
{
    const int MAX = 1000000;

    // let C(n) = the Collatz function applied to n
    // let L(n) = length of the Collatz chain starting at n

    // initialize all chain lengths to -1 except for i=0 (corresponding to L(1)) which is 1
    int* chain_len = new int[MAX+1];
    chain_len[0] = 0;
    chain_len[1] = 1;
    for( int i = 2; i <= MAX; i++ )
        chain_len[i] = -1;

    int num_with_biggest_chain = 1;

    // for an new integer n s.t. L(n) is unknown, start computing the chain at n: c_0 = n, c_1 = C(n), c_2 = C(C(n)), etc.
    for( int i = 2; i <= MAX; i++ )
    {
//        cerr << i << ": chain length is " << chain_len[i] << endl;

        // if n's chain length is already known, check to see if it is bigger than the biggest known chain length so far
        if( chain_len[i] > 0 )
        {
            if( chain_len[i] > chain_len[num_with_biggest_chain] )
            {
                num_with_biggest_chain = i;
            }
            continue;
        }

        uint64_t n = i; // n is the integer whose chain length we are computing
        vector<uint64_t> current_chain;

        // if L(c_j) is unknown, add it to the list of numbers whose chain length we're computing, and compute c_{j+1} = C(c_j)
        while( n > MAX || chain_len[n] < 0 )
        {
            current_chain.push_back(n);
            n = collatz(n);
//            cerr << "n=" << n << endl;
        }

        int last_len = chain_len[n];
//        cerr << "current_chain.back() = " << current_chain.back() << endl;
//        cerr << "last_len = " << last_len << endl;
        int count = 1;

        // if L(c_j) is *known*, then set c_{j-k} = L(c_j)+k for all k = 1 to j.
        while( current_chain.size() > 0 )
        {
            // only update the chain length of current_chain.back() if it is within the set of values we're considering
            if( current_chain.back() <= MAX )
            {
                chain_len[current_chain.back()] = last_len + count;
//                cerr << "chain length of " << current_chain.back() << " is now " << chain_len[current_chain.back()] << endl;
            }
            current_chain.pop_back();
            ++count;
        }

        if( chain_len[i] > chain_len[num_with_biggest_chain] )
        {
            num_with_biggest_chain = i;
        }
    }

    cout << num_with_biggest_chain << " has the longest Collatz chain length: " << chain_len[num_with_biggest_chain] << endl;

    delete chain_len;

    return 0;
}

uint64_t collatz(uint64_t n)
{
    if( n%2 == 0 ) return n/2;
    else return 3*n+1;
}

// EOF
