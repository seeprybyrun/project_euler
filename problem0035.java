import java.util.ArrayList;
import java.util.List;

public class Problem0035 {
	public static List<Integer> primes = null;
	
	public static void main(String[] args) {
		final int UPPER_BOUND = 1000000;
		primes = allPrimesLessThan(UPPER_BOUND);
		System.out.println(primes.size());
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
	
}