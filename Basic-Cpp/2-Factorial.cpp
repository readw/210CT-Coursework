/*
Count the number of trailing 0s (number of 0s at the end of the number) in a
factorial number.

Example: Input: 5, Output: 1; Input: 10, Output: 2.
*/

#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;

int Factorial(int number){
    int zeros = 0;
    
    for (int i = 1; i != number; i++){
        zeros += number/pow(5,i);
    }
    
    return zeros;
}

int main() {
    int input;
    cout << "Enter a number: ";
    cin >> input;
    cout << "Output: " << Factorial(input) << endl;
    
    return 0;
}
