/* 
Week 1 - 1) Write a function that randomly shuffles the array of integers and
            explain the rationale behind its implementation.
*/

#include <iostream>
#include <cstdlib>
#include <vector>
using namespace std;

vector<int> Randomise(vector<int> &data) {
    /* Function to randomise the order of a vector. */
    int index = 0; /* Default index to first item */
    int length = data.size(); /* Get length of vector. */
    int randomIndex = 0; /* Set default randomIndex as 0 */
    vector<int> randomList;
    while (index++ < length){
        randomIndex = (rand()%(data.size())); /* Generate a random value of an index in the array. */
        randomList.insert(randomList.begin(),data[randomIndex]); /* Insert in new vector randomList particular vector. */
        data.erase(data.begin()+randomIndex); /* Erase the item that has been inserted so it isn't picked again. */
    }
    
    return randomList;
}

int main() {
    /* Predefine creation of vector. */
    int value, number;
    vector<int> data;
    
    
    cout << "Enter length of list: ";
    cin >> value;
    
    /* Input numbers that are appended to a vector. */
    for (int i = 0; i < value; i++) {
        cout << "Enter a number: ";
        cin >> number;
        data.insert(data.begin()+i,number);
    }
    
    vector<int> randomResult = Randomise(data);
    for (int i = 0; i < randomResult.size(); i++){
        cout << randomResult[i] << " ";
    }
    cout << endl;
    return 0;
}
