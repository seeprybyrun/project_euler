/*
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
*/

import java.util.ArrayList;
import java.util.List;

public class problem0023 {
	public static void main(String[] args) {
		final int UPPER_BOUND = 28123;
		List<Integer> abundants = allAbundantNumbersLessThan(UPPER_BOUND);
		boolean[] sumOfAbundants = new boolean[UPPER_BOUND];
		for( int i = 0; i < abundants.size(); i++ ) {
			for( int j = 0; j < abundants.size(); j++ ) {
				int k = abundants.get(i)+abundants.get(j);
				if( k < UPPER_BOUND ) {
					sumOfAbundants[k] = true;
				}
			}
		}
		
		int total = 0;
		for( int i = 0; i < UPPER_BOUND; i++ ) {
			if( !sumOfAbundants[i] ) total += i;
		}
		System.out.println(total);
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
	
	public static boolean isAbundant(int n) {
		return sumOfProperDivisors(n) > n;
	}
	
	public static List<Integer> allAbundantNumbersLessThan(int n) {
		List<Integer> abundants = new ArrayList<Integer>();
		for( int i = 1; i < n; i++ ) {
			if( isAbundant(i) ) {
				abundants.add(abundants.size(),i);
			}
		}
		return abundants;
	}
	
}