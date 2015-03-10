/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

bool isPrime(uint64_t n);
uint64_t mulmod(uint64_t a, uint64_t b, uint64_t m);
uint64_t powmod(uint64_t a, uint64_t b, uint64_t m);
uint64_t largestPowerOfTwo(uint64_t n);

int main ()
{
    uint64_t N = 600851475143;

    // initial check whether N is divisible by 2 or 3
    uint64_t biggestPrimeFactor = 1;
    if( N % 2 == 0 ) {
        biggestPrimeFactor = 2;
        cout << "prime factor: 2" << endl;
    }
    if( N % 3 == 0 ) {
        biggestPrimeFactor = 3;
        cout << "prime factor: 3" << endl;
    }

    const uint64_t n = floor(sqrt(N));
    for( uint64_t i = 2; i <= n; i++ )
    {
        // only check factors of form 6*i +- 1 to be prime factors
        if(N % i != 0) continue;
        uint64_t p1 = i;
        uint64_t p2 = N/i;

        cout<< "factors:" << p1 << "," << p2 << endl;

        if( (p1%6==1 || p1%6==5) && isPrime(p1) && p1 > biggestPrimeFactor ){
            biggestPrimeFactor = p1;
            cout << "prime factor: " << p1 << endl;
        }
        if( (p2%6==1 || p2%6==5) && isPrime(p2) && p2 > biggestPrimeFactor ){
            biggestPrimeFactor = p2;
            cout << "prime factor: " << p2 << endl;
        }
    }

    cout << biggestPrimeFactor;

    return 0;
}

// implements Miller-Rabin primality test to probability 1-4^{-ITERATIONS}
bool isPrime(uint64_t n) {
    const uint64_t ITERATIONS = 50;
    uint64_t s = largestPowerOfTwo(n-1);
    uint64_t S = pow(2,s);
    uint64_t d = (n-1)/S; // d is largest odd divisor of n-1

    srand( (unsigned) time(0) );

    for( uint64_t i = 0; i < ITERATIONS; i++ ) {
        uint64_t a = (rand()%(n-1))+1; // 1 <= a <= n-1
        // if a^d != 1 (mod n) AND a^{2^r * d} != -1
        //   (mod n) for all 0 <= r <= s-1, then
        //   a is a witness to n's compositeness;
        // if n is composite, then a will fail to be witness with <= 1/4 probability;
        // if n is prime, then a will always fail to be witness
        if(powmod(a,d,n) != 1) {
            bool isWitness = true;
            for( uint64_t R=1; R < S; R*=2 ) {
                if(powmod(a,R*d,n) == n-1) {
                    isWitness = false;
                    break;
                }
            }
            if(isWitness) return false;
        }
    }
    // if n survives against ITERATIONS putative witnesses, then we
    //   presume n is prime (with very high probability, anyway!)
    return true;

}

uint64_t largestPowerOfTwo(uint64_t n) {

    uint64_t count = 0;
    while( n % 2 == 0 ) {
        count += 1;
        n /= 2;
    }
    return count;

}

// Russian peasant multiplication
uint64_t mulmod(uint64_t a, uint64_t b, uint64_t m) {
    uint64_t res = 0;
    while (a != 0) {
        if (a & 1) res = (res + b) % m;
        a >>= 1;
        b = (b << 1) % m;
    }
    return res;
}

uint64_t powmod(uint64_t a, uint64_t b, uint64_t m) {
    uint64_t res = 1;
    while (b != 0) {
        if (b & 1) res = (res * a) % m;
        b >>= 1;
        a = mulmod(a,a,m);
    }
    return res;
}

// EOF
