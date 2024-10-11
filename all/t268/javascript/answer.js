function canCompleteCircuit(gas, cost) {
    /**
     * Determines if there exists a starting gas station's index where you can travel
     * around the circuit once in a clockwise direction.
     *
     * @param {number[]} gas - Array of integers representing the amount of gas at each station.
     * @param {number[]} cost - Array of integers representing the cost of gas to travel from each station to the next.
     * @returns {number} - The starting gas station's index if the circuit can be completed, otherwise -1.
     */

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