""" 
Two City Scheduling
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], 
the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
"""

def twoCitySchedCost(costs):
    costs.sort(key=lambda x: x[0] - x[1])
    n = len(costs) // 2
    dp = [[float('inf')] * (n + 1) for _ in range(2*n + 1)]
    dp[0][0] = 0
    
    for i in range(1, 2*n + 1):
        for j in range(max(0, i - n), min(n, i) + 1):
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + costs[i-1][0])
            if j < i:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + costs[i-1][1])
                
    return dp[2*n][n]

print(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))