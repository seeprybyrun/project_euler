/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
using namespace std;

bool isPalindrome(int n);

int main ()
{
    int biggestPalindrome = -1;
    const int MAXPOWEROFTEN = 3;

    for( int x = 2*(pow(10,MAXPOWEROFTEN)-1); x >= 2*(pow(10,MAXPOWEROFTEN-1)); x-- ) {

 //       cout << x << endl;

        if( x%2 == 0 ){
            // moving diagonally / starting just above the main \ diagonal and moving up and to the right
            for( int d = 0; d < min((int)(pow(10,MAXPOWEROFTEN)*2-x)/2,x/2); d++ ) {
//                cout << x/2+d << "," << x/2-d << endl;
                int t = (x/2+d)*(x/2-d);
                if(t > biggestPalindrome && isPalindrome(t)) biggestPalindrome = t;
            }
        }
        if( x%2 == 1 ){
            // moving diagonally / starting on the main \ diagonal and moving up and to the right
            for( int d = 0; d < min((int)(pow(10,MAXPOWEROFTEN)*2-x)/2,x/2); d++ ) {
//                cout << (x+1)/2+d << "," << (x-1)/2-d << endl;
                int t = ((x+1)/2+d)*((x-1)/2-d);
                if(t > biggestPalindrome && isPalindrome(t)) biggestPalindrome = t;
            }
        }

    }

    cout << "Biggest palindrome: " << biggestPalindrome << endl;

    return 0;
}

bool isPalindrome(int n) {

    //string s = to_string(n);
    string s = static_cast<ostringstream*>( &(ostringstream() << n))->str();
//    cout << "The number " << s;
    int len = s.length();
    bool isPal = true;
    for( int i = 0; i < (len+1)/2; i++ ){
        if(s[i] != s[len-i-1]) {
            isPal = false;
            break;
        }
    }

//    if(isPal) cout << " is a palindrome" << endl;
//    else cout << " is NOT a palindrome" << endl;

    return isPal;

}

// EOF
