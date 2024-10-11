package org.real.temp;

import java.util.List;

public class Answer {
    public static int canCompleteCircuit(List<Integer> gas, List<Integer> cost) {
        /**
         * Determines if there exists a starting gas station's index where you can travel
         * around the circuit once in a clockwise direction.
         *
         * @param gas  List of integers representing the amount of gas at each station.
         * @param cost List of integers representing the cost of gas to travel from each station to the next.
         * @return The starting gas station's index if the circuit can be completed, otherwise -1.
         */

        int totalGas = 0;
        int currentGas = 0;
        int startStation = 0;

        for(int i = 0; i < gas.size(); i++) {
            totalGas += gas.get(i) - cost.get(i);
            currentGas += gas.get(i) - cost.get(i);

            if(currentGas < 0) {
                startStation = i + 1;
                currentGas = 0;
            }
        }

        return totalGas >= 0 ? startStation : -1;
    }
}