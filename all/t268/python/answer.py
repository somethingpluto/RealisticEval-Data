from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    n = len(gas)
    total_gas = total_cost = tank = start_index = 0

    for i in range(n):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]

        if tank < 0:  # If tank becomes negative, update start_index and reset tank
            start_index = i + 1
            tank = 0

    return start_index if total_gas >= total_cost else -1
