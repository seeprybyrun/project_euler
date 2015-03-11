/*
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
*/

import java.util.ArrayList;
import java.util.List;

public class problem0021 {
	public static void main(String[] args) {
//		List<Integer> divs = divisors(220);
//		for( int i = 0; i < divs.size(); i++ ) {
//			System.out.println(divs.get(i));
//		}
//		System.out.println(sumOfDivisors(220));
//		System.out.println(sumOfProperDivisors(220));
//		System.out.println(areAmicable(220,284));
		
		List<Integer> amicableNums = findAmicableNumbers(10000);
		int sum = 0;
		for( int i = 0; i < amicableNums.size(); i++ ) {
			System.out.println(amicableNums.get(i));
			sum += amicableNums.get(i);
		}
		System.out.println("Sum: " + sum);
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
	
	public static boolean areAmicable(int a, int b) {
		return (a != b && a == sumOfProperDivisors(b) && b == sumOfProperDivisors(a));
	}
	
	public static List<Integer> findAmicableNumbers(int upperBound) {
		List<Integer> amicableNums = new ArrayList<Integer>();
		for( int i = 1; i <= upperBound; i++ ) {
			int j = sumOfProperDivisors(i);
			if( areAmicable(i,j) ) {
				amicableNums.add(amicableNums.size(),i);
				// don't need to add j simultaneously
			}
		}
		return amicableNums;
	}
}