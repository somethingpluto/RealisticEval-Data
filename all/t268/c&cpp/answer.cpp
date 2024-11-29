#include <vector>
#include <algorithm>

int can_complete_circuit(const std::vector<int>& gas, const std::vector<int>& cost) {
    int n = gas.size();
    int total_gas = 0;
    int total_cost = 0;
    int tank = 0;
    int start_index = 0;

    for (int i = 0; i < n; ++i) {
        total_gas += gas[i];
        total_cost += cost[i];
        tank += gas[i] - cost[i];

        if (tank < 0) {  // If tank becomes negative, update start_index and reset tank
            start_index = i + 1;
            tank = 0;
        }
    }

    return (total_gas >= total_cost) ? start_index : -1;
}
