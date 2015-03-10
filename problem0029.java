import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Problem0029 {
	public static List<Integer> primes = null;
	
	public static void main(String[] args) {
		final int UPPER_BOUND = 101;
		primes = allPrimesLessThan(UPPER_BOUND);
		
		List<int[]> allPrimeFacts = new ArrayList<int[]>();
		
		for( int a = 2; a < UPPER_BOUND; a++ ) {
			int[] primeFact = primeFactorization(a);
			for( int b = 2; b < UPPER_BOUND; b++ ) {
				int[] expPrimeFact = new int[primes.size()];
				for( int i = 0; i < primes.size(); i++ ) {
					expPrimeFact[i] = primeFact[i] * b;
				}
				allPrimeFacts.add(expPrimeFact);
			}
		}
		
		// need a way of sorting and comparing these arrays of ints
		Collections.sort(allPrimeFacts,new ArrayComparator());
		
//		for( int i = 0; i < allPrimeFacts.size(); i++ ) {
//			String toPrint = "[";
//			int[] fact = allPrimeFacts.get(i);
//			for( int j = 0; j < fact.length; j++ ) {
//				toPrint += fact[j] + ",";
//			}
//			toPrint += "]";
//			System.out.println(toPrint);
//		}

		// then count number of distinct elements
		int distinctFacts = 0;
		int[] prevFact = null;
		ArrayComparator ac = new ArrayComparator();
		for( int i = 0; i < allPrimeFacts.size(); i++ ) {
			int[] thisFact = allPrimeFacts.get(i);
			if( prevFact == null || ac.compare(prevFact,thisFact) != 0) {
				distinctFacts++;
			}
			prevFact = thisFact;
		}
		System.out.println(distinctFacts);
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
	
	public static boolean isPrime(int n) {
		return sumOfProperDivisors(n) == 1;
	}
	
	public static List<Integer> allPrimesLessThan(int n) {
		List<Integer> primes = new ArrayList<Integer>();
		for( int i = 2; i < n; i++ ) {
			if( isPrime(i) ) {
				primes.add(i);
			}
		}
		return primes;
	}
	
	public static int[] primeFactorization(int n) {
		int[] factorization = new int[primes.size()];
		
		//String toPrint = "factorization of " + n + " is: ";
		for( int i = 0; i < primes.size(); i++ ) {
			int p = primes.get(i);
			int q = p;
			int power = 1;
			while( n % q == 0 ) {
				//System.out.println(q);
				q *= p;
				power += 1;
			}
			factorization[i] = power-1;
			//toPrint += p + "^" + factorization[i] + " ";
		}
		//System.out.println(toPrint);
		return factorization;
	}
	
	static class ArrayComparator implements Comparator<int[]> {
		public int compare( int[] a, int[] b ) {
			if( a.length < b.length ) return -1;
			if( a.length > b.length ) return  1;
			for( int i = 0; i < a.length; i++ ) {
				if( a[i] < b[i] ) return -1;
				if( a[i] > b[i] ) return  1;
			}
			return 0;
		}
	}
	
}