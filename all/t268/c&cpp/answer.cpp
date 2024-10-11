#include <vector>
using namespace std;

int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
    int total_gas = 0;
    int current_gas = 0;
    int start_station = 0;

    for(int i=0; i<gas.size(); i++){
        total_gas += gas[i] - cost[i];
        current_gas += gas[i] - cost[i];

        // If current gas becomes negative, we need to reset our start station
        if(current_gas < 0){
            start_station = i + 1;
            current_gas = 0;
        }
    }

    // If total gas is less than zero, it means we cannot complete the circuit
    return (total_gas >= 0)? start_station : -1;
}