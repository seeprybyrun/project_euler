/*
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
    3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
    (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
*/

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;
string spelling(int n);

int main ()
{
    const int MAX = 1000;
    int total_letters = 0;

    for( int i = 1; i <= MAX; i++ )
    {
        string s = spelling(i);
        cout << s << endl;
        total_letters += s.length();
    }


    cout << total_letters << endl;

    return 0;
}

// assumes 1 <= n < 10000
string spelling(int n)
{
    if( n < 1 || n > 10000 )
        return "";

    const string ONE_S = "one";
    const string TWO_S = "two";
    const string THREE_S = "three";
    const string FOUR_S = "four";
    const string FIVE_S = "five";
    const string SIX_S = "six";
    const string SEVEN_S = "seven";
    const string EIGHT_S = "eight";
    const string NINE_S = "nine";
    const string TEN_S = "ten";
    const string ELEVEN_S = "eleven";
    const string TWELVE_S = "twelve";
    const string THIRTEEN_S = "thirteen";
    const string FOURTEEN_S = "fourteen";
    const string FIFTEEN_S = "fifteen";
    const string SIXTEEN_S = "sixteen";
    const string SEVENTEEN_S = "seventeen";
    const string EIGHTEEN_S = "eighteen";
    const string NINETEEN_S = "nineteen";
    const string TWENTY_S = "twenty";
    const string THIRTY_S = "thirty";
    const string FORTY_S = "forty";
    const string FIFTY_S = "fifty";
    const string SIXTY_S = "sixty";
    const string SEVENTY_S = "seventy";
    const string EIGHTY_S = "eighty";
    const string NINETY_S = "ninety";
    const string HUNDRED_S = "hundred";
    const string THOUSAND_S = "thousand";
    const string AND_S = "and";

    if( n == 1000 ) return ONE_S + THOUSAND_S;
    else if( n >= 100 )
    {
        if( n%100 == 0 ) return spelling(n/100) + HUNDRED_S;
        else return spelling(n/100) + HUNDRED_S + AND_S + spelling(n%100);
    }
    else if( n%10 == 0 ) switch(n)
    {
        case 10:
            return TEN_S;
        case 20:
            return TWENTY_S;
        case 30:
            return THIRTY_S;
        case 40:
            return FORTY_S;
        case 50:
            return FIFTY_S;
        case 60:
            return SIXTY_S;
        case 70:
            return SEVENTY_S;
        case 80:
            return EIGHTY_S;
        case 90:
            return NINETY_S;
    }
    else if( n > 10 && n < 20 ) switch(n)
    {
        case 11:
            return ELEVEN_S;
        case 12:
            return TWELVE_S;
        case 13:
            return THIRTEEN_S;
        case 14:
            return FOURTEEN_S;
        case 15:
            return FIFTEEN_S;
        case 16:
            return SIXTEEN_S;
        case 17:
            return SEVENTEEN_S;
        case 18:
            return EIGHTEEN_S;
        case 19:
            return NINETEEN_S;
    }
    else if( n < 10 ) switch(n)
    {
        case 1:
            return ONE_S;
        case 2:
            return TWO_S;
        case 3:
            return THREE_S;
        case 4:
            return FOUR_S;
        case 5:
            return FIVE_S;
        case 6:
            return SIX_S;
        case 7:
            return SEVEN_S;
        case 8:
            return EIGHT_S;
        case 9:
            return NINE_S;
    }
    else return spelling(10 * (n/10)) + spelling(n%10);
}

// EOF
