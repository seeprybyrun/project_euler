/*
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
*/

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

class Date
{
    int month;
    int day;
    int year;
public:
    Date(int mm=1, int dd=1, int yyyy=1900) {month=mm; day=dd; year=yyyy;}
    ~Date() {};
    int getMonth() const {return month;}
    int getDay() const {return day;}
    int getYear() const {return year;}

    void addDays(int n);
};
int daysInMonth(const Date &d);
int daysInYear(const Date &d);
bool isLeapYear(const Date &d);

int main ()
{
    int first_of_months = 0;
    Date d(12,31,1899); // this is a Sunday

    while( d.getYear() <= 2000 )
    {
        d.addDays(7);
        if( d.getYear() >= 1901 && d.getYear() <= 2000 && d.getDay()==1 )
        {
            ++first_of_months;
            cout << d.getMonth() << "/" << d.getYear() << endl;
        }
    }

    cout << first_of_months << endl;

    return 0;
}

void Date::addDays(int n)
{
    if( n < 0 )
    {
        return; // do nothing if n < 0
    }

    // if enough days to get to first of month, advance there
    while( n >= daysInMonth(*this) - this->day + 1 )
    {
        // if it's the first of the year and there are enough days to go to the next year, do that instead
        if( this->month == 1 && this->day == 1 && n >= daysInYear(*this) )
        {
            n -= daysInYear(*this);
            ++this->year;
        }
        // otherwise just advance to the first of the next month
        else
        {
            n -= daysInMonth(*this) - this->day + 1;
            this->day = 1;
            ++this->month;
            // advance the year if we pass to Jan 1
            if( this->month > 12 ) { this->year+=1; this->month = 1; }
        }
    }
    // finally, just increment the day by whatever amount is left
    this->day += n;

    return;
}

bool isLeapYear(const Date &d)
{
    int yy = d.Date::getYear();
    if( yy%400==0 || ( yy%4==0 && yy%100!=0 ) )
        return true;

    return false;
}

int daysInYear(const Date &d)
{
    return 365 + (isLeapYear(d)?1:0);
}

int daysInMonth(const Date &d)
{
    int mm = d.getMonth();

    if( mm==2 && isLeapYear(d) )
        return 29;
    if( mm==2 && !isLeapYear(d) )
        return 28;
    if( mm==4 || mm==6 || mm==9 || mm==11 )
        return 30;
    return 31;
}

// EOF
