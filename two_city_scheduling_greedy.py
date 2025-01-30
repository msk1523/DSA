""" 
Two City Scheduling
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], 
the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
"""

def twoCitySchedCost(costs):
    #write code here
    costs.sort(key = lambda x: x[0]-x[1])
    n = len(costs)
    cost = 0
    
    for i in range(n//2):
        cost+=costs[i][0]
        
    for i in range(n//2,n):
        cost+=costs[i][1]

    return cost