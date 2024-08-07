"""
There are n gas stations along a circular route,
where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and
it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost,
return the starting gas station's index 
if you can travel around the circuit once in the clockwise direction,
otherwise return -1. If there exists a solution, it is guaranteed to be unique
"""

from typing import List

class Solution:
    #code generated with chatgpt
    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     n = len(gas)

    #     for i in range(n):
    #         current_gas_cost = 0
    #         fuel = 0
    #         print(i)
    #         for j in range(i, i + n):
    #             k = j % n
    #             # print(f'{k} = {j}%{n} ==> {j%n}')
    #             fuel = gas[k] - cost[k]
    #             if current_gas_cost + fuel < 0:
    #                 break
    #             current_gas_cost += fuel
    #             # print(current_gas_cost)
    #         else:
    #             return i
    #     return -1


    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
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
        



s = Solution()
# gas = [4,5,2,6,5,3]
# cost = [3,2,7,3,2,9]
gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
gas = [2,3,4]
cost = [3,4,3]
print(s.canCompleteCircuit(gas=gas,cost=cost))
# print(s.canCompleteCircuit(gas=[1,2,3,4,5],cost=[3,4,5,1,2]))