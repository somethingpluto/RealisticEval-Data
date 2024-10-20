package org.real.temp;

import java.util.List;

public class Answer {


    /**
     * Determines if there is a starting gas station index at which a car can complete the circuit.
     * 
     * @param gas An array representing the amount of gas at each station.
     * @param cost An array representing the cost of gas to travel from each station to the next one.
     * @return The starting gas station index if the car can complete the circuit, or -1 otherwise.
     */
    public static int canCompleteCircuit(List<Integer> gas, List<Integer> cost) {
        int n = gas.size();
        int totalGas = 0, totalCost = 0, tank = 0, startIndex = 0;

        for (int i = 0; i < n; i++) {
            totalGas += gas.get(i);
            totalCost += cost.get(i);
            tank += gas.get(i) - cost.get(i);

            if (tank < 0) {  // If tank becomes negative, update startIndex and reset tank
                startIndex = i + 1;
                tank = 0;
            }
        }

        return totalGas >= totalCost ? startIndex : -1;
    }
}