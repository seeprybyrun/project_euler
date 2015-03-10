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