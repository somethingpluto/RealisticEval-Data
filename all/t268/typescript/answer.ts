function canCompleteCircuit(gas: number[], cost: number[]): number {
    let totalGas = 0;
    let currentGas = 0;
    let startStation = 0;

    for(let i = 0; i < gas.length; i++) {
        totalGas += gas[i] - cost[i];
        currentGas += gas[i] - cost[i];

        if(currentGas < 0) {
            startStation = i + 1;
            currentGas = 0;
        }
    }

    return totalGas >= 0 ? startStation : -1;
}