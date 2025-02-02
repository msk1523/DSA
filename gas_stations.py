""" 
Gas Stations
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:-
Input: gas = [2, 3, 4, 5, 1], cost = [3, 4, 2, 1, 4]
Expected Output: 4
Explanation:
Start at station 4 (index 4) and fill up with 1 unit of gas. Your tank starts at 0 + 1 = 1.
Travel to station 0. Your tank = 1 - 4 + 2 = -1 (not enough to reach station 0 from station 4 directly, but consider the circuit logic and find the correct path).
Start from the proposed solution and verify:
Start at station 4 (index 4) with 1 unit of gas.
Travel to station 0. Your tank = 1 - 4 (negative, but let's find where the loop actually works):
Fill up at station 0: 1 + 2 = 3.
Travel to station 1. Your tank = 3 - 3 + 3 = 3.
Travel to station 2. Your tank = 3 - 4 + 4 = 3.
Travel to station 3. Your tank = 3 - 2 + 5 = 6.
Travel back to station 4. Your tank = 6 - 1 + 1 = 6.

Therefore, the tank never runs dry when starting from station 4, and this station allows completing the circuit. Thus, return 4 as the starting index.
"""

def canCompleteCircuit(gas, cost):
    n = len(gas)
    
    for i in range(n):
        cost_for_next_station = 0
        can_complete = True
        
        for j in range(n):
            pos = (i + j) % n 
            cost_for_next_station += gas[pos] - cost[pos]
            
            if cost_for_next_station < 0:
                can_complete = False
                break
        
        if can_complete:
            return i
        
    return -1

print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))