/*
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total
from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                              75
                            95  64
                          17  47  82
                        18  35  87  10
                      20  04  82  47  65
                    19  01  23  75  03  34
                  88  02  77  73  07  63  67
                99  65  04  28  06  16  70  92
              41  41  26  56  83  40  80  70  33
            41  48  72  33  47  32  37  16  94  29
          53  71  44  65  25  43  91  52  97  51  14
        70  11  33  28  77  73  17  78  39  68  17  57
      91  71  52  38  17  14  91  43  58  50  27  29  48
    63  66  04  68  89  53  67  30  73  16  69  87  40  31
  04  62  98  27  23  09  70  98  73  93  38  53  60  04  23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
*/

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;
vector< vector<int> > read_grid( string filename );

int main ()
{
    // idea: dynamic programming algorithm, reading in rows one at a time (going from bottom to top)
    // row 0 = bottommost row, cell 0 = leftmost cell in row
    // let v(k,i) = value of cell at row k, cell i
    // let m(k,i) = highest-valued path to row k, cell i
    // then m(0,i) = v(0,1)
    // and m(k,i) = max(m(k-1,i),m(k-1,i+1)) + v(k,i)

    string filename = "problem18.txt";
    vector< vector<int> > v = read_grid(filename);

    int len = v.size();
    int** max_path = new int*[len+1];
    for(int i = 0; i < len; i++)
    {
        max_path[i] = new int[v[i].size()];
        for( int j = 0; j < v[i].size(); j++ )
            max_path[i][j] = -1;
    }

    // initializes an extra row of ints below the bottom row which will all be 0
    max_path[len] = new int[v[len-1].size()+1];
    for( int j = 0; j < v[len-1].size()+1; j++)
        max_path[len][j] = 0;

    // starts at bottommost row of triangle
    for( int i = len-1; i >= 0; i--)
    {
        // iterates from left to right along the row
        for( int j = 0; j < v[i].size(); j++)
        {
            max_path[i][j] = max( max_path[i+1][j], max_path[i+1][j+1] ) + v[i][j];
            cout << max_path[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}

// reads in a grid of integers (possibly with different numbers of integers per line), separated by spaces and newlines
vector< vector<int> > read_grid( string filename )
{
    vector< vector<int> > ret;

    ifstream f1( filename.c_str() );
    if( f1.is_open() )
    {
        while( f1.good() )
        {
            string line;
            vector<int> v;

            getline(f1,line);
            char tokenized_line[line.length()+1];
            strcpy( tokenized_line, line.c_str() );
            char *pch = strtok( tokenized_line, " " );

            // how do I iterate through a tokenized string?
            do
            {
                v.push_back( atoi(pch) );
//                cerr << v.back() << " ";
                pch = strtok( NULL, " " );
            } while( pch != NULL );
//                cerr << endl;

            ret.push_back(v);
        }
        f1.close();
    }

    return ret;
}

// EOF
