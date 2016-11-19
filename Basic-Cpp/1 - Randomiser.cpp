/* #include <iostream>
#include <cstdlib>
#include <vector>
using namespace std;

vector<int> Randomiser(vector<int> &data) {
    int i = 0;
    int length = data.size();
    int randomI = 0;
    vector<int> randomList;
    while (i++ < length){
        randomI = (rand()%(data.size()));
        randomList.insert(randomList.begin(),data[randomI]);
        data.erase(data.begin()+randomI);
    }
    
    return randomList;
}

int main() {
    int value, number;
    vector<int> data;
    
    cout << "Enter length of list: ";
    cin >> value;
    
    for (int i = 0; i < value; i++) {
        cout << "Enter a number: ";
        cin >> number;
        data.insert(data.begin()+i,number);
    }
    
    vector<int> randomResult = Randomiser(data);
    for (int i = 0; i < randomResult.size(); i++){
        cout << randomResult[i] << " ";
    }
    cout << endl;
    return 0;
} */