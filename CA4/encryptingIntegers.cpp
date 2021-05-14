#include <iostream>
#include <string>
#include <vector>
using namespace std;
int gcd(int a, int b)
{
    // Everything divides 0
    if (a == 0)
       return b;
    if (b == 0)
       return a;
  
    // base case
    if (a == b)
        return a;
  
    // a is greater
    if (a > b)
        return gcd(a-b, b);
    return gcd(a, b-a);
}

int main(void){
    int first_start=0, first_end=0, second_start=0, second_end=0;
    cout << "First line: ";
    cin >> first_start >> first_end;
    cout << "Second line: ";
    cin >> second_start >> second_end;
    int line1_diff = first_end -first_start, line2_diff = second_end-second_start;
    
    vector<int> first_array , second_array;
    vector< pair <int,int> > result;
    for(int i = 0; i <= line1_diff; i++)
    {
        first_array.push_back(first_start+i);
    }
    for(int i = 0; i <= line2_diff; i++)
    {
        second_array.push_back(second_start+i);
    }

    for(auto i: first_array)
    {
        for(auto j: second_array)
        {
            
            if( gcd(i, j) ==1){
                result.push_back(make_pair(i, j));
            }
        }
    }
    cout << result.size() << endl;
}