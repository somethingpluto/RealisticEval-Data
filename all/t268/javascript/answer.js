function canCompleteCircuit(gas, cost) {
    const n = gas.length;
    let totalGas = 0;
    let totalCost = 0;
    let tank = 0;
    let startIndex = 0;

    for (let i = 0; i < n; i++) {
        totalGas += gas[i];
        totalCost += cost[i];
        tank += gas[i] - cost[i];

        if (tank < 0) {  // If tank becomes negative, update startIndex and reset tank
            startIndex = i + 1;
            tank = 0;
        }
    }

    return totalGas >= totalCost ? startIndex : -1;
}