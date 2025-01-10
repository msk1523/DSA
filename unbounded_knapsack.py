# Unbounded Knapsack
# Given a set of N items, each with a weight and a value, represented by the array w and val respectively. Also, a knapsack with weight limit W.

# The task is to fill the knapsack in such a way that we can get the maximum profit. Return the maximum profit.

# Note: Each item can be taken any number of times.



# Input: 
# N = 2
# W = 3
# val = [4, 2]
# wt = [3, 1]
# Output: 3
# Explanation: 
# 1.Pick the 2nd element thrice.
# So, Total value = 2 + 2 + 2 = 6. and the total weight = 1 + 1 + 1  = 3 
# which is <= 3.

def knapSack(N, W, val, wt):
    #write code here
    dp=[[0]*(W+1)for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,W+1):
            exclude=dp[i-1][j]
            include=0
            if wt[i-1]<=j:
                include=val[i-1]+dp[i][j-wt[i-1]]
            dp[i][j]=max(include,exclude)
    return dp[N][W]

print(knapSack(2,3,[4,2],[3,1]))