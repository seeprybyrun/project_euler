/*
Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n^2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
*/

import java.util.ArrayList;
import java.util.List;

public class problem0027 {
	public static void main(String[] args) {
		final int UPPER_BOUND = 1000;
		final int LOWER_BOUND = -UPPER_BOUND;
		boolean[] isPrime = new boolean[UPPER_BOUND];
		for( int i = 0; i < UPPER_BOUND; i++ ) {
			if( sumOfProperDivisors(i) == 1 ) isPrime[i] = true;
			else isPrime[i] = false;
		}
		
		int maxConsecPrimes = 0;
		int bestProduct = 0;
		
		for( int a = LOWER_BOUND + 1; a < UPPER_BOUND; a++ ) {
			for( int b = 0; b < isPrime.length; b++ ) {
				int n = 0;
				while( true ) {
					int p = n*n + a*n + b;
					if( 0 < p && ((p < UPPER_BOUND && isPrime[p] || sumOfProperDivisors(p) == 1 ))){
						n++;
					}
					else {
						break;
					}
				}
				if( n > maxConsecPrimes ) {
					maxConsecPrimes = n;
					bestProduct = a*b;
				}
			}
		}
		System.out.println("best product: " + bestProduct);
		System.out.println("num consecutive primes: " + maxConsecPrimes);
	}
	
	public static List<Integer> divisors(int n) {
		List<Integer> divs = new ArrayList<Integer>();
		for( int i = 1; i <= Math.sqrt(n); i++ ) {
			if( n % i == 0 ) {
				divs.add(divs.size(),i);
				if( n/i != i ) divs.add(divs.size(),n/i);
			}
		}
		divs.sort(null); // sorts list of divisors in ascending order
		return divs;
	}
	
	public static int sumOfDivisors(int n) {
		List<Integer> divs = divisors(n);
		int sum = 0;
		for( int i = 0; i < divs.size(); i++ ) {
			sum += divs.get(i);
		}
		return sum;
	}
	
	public static int sumOfProperDivisors(int n) {
		return sumOfDivisors(n) - n;
	}
	
}