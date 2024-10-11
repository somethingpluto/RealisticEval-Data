#include <iostream>
using namespace std;

int calculateTotalSeconds(int time[], int size) {
    if(size > 4 || size <= 0){
        cout << "Invalid input! Please enter an array with elements between 1 and 4.";
        return -1;
    }

    int total_seconds = 0;
    for(int i=0; i<size; ++i){
        switch(i){
            case 0: total_seconds += time[i]*24*60*60; break;
            case 1: total_seconds += time[i]*60*60; break;
            case 2: total_seconds += time[i]*60; break;
            case 3: total_seconds += time[i]; break;
            default: break;
        }
    }

    return total_seconds;
}
