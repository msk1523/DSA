# Minimum Cost Climbing Stairs
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

# Example 1:

# Input: cost = [10,20,30]
# Output: 20
# Explanation: You will start at index 1.
# - Pay 20 and climb two 

def minCostClimbingStairs(cost):
    #write code here
    n=len(cost)
    mincost=[0]*(n+1)
    mincost[0]=0
    mincost[1]=0
    for i in range(2,n+1):
        onestep=cost[i-1]+mincost[i-1]
        twostep=cost[i-2]+mincost[i-2]
        mincost[i]=min(onestep,twostep)
    return mincost[n]

print(minCostClimbingStairs([10, 15, 20]))#15