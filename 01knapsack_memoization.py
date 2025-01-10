# 01 Knapsack
# You are provided with a set of N items, each with a specified weight and value. Your objective is to pack these items into a backpack with a weight limit of W, maximizing the total value of items in the backpack. Specifically, you have two arrays: val[0..N-1], representing the values of the items, and wt[0..N-1], indicating their weights. Additionally, you have a weight limit W for the backpack. The challenge is to determine the most valuable combination of items where the total weight does not exceed W. Note that each item is unique and indivisible, meaning it must be either taken as a whole or left entirely.



# Input:
# N = 3
# W = 8
# values[] = [2,3,9]
# weight[] = [8,2,5]
# Output: 12
# Explanation: Choose the last 2 items that weighs 2 and 5 units respectively and hold values 3 and 9 that add up to 12. 

def knapSack(W, wt, val, n):
    dp = [[-1]* (W+1) for _ in range(n)]
    def helper(index, rem_weight):
        #base case
        if index > n-1 or rem_weight ==0:
            return 0
        if dp[index][rem_weight]!=-1:
            return dp[index][rem_weight]
        #recursive case
        exclude = helper(index+1, rem_weight)
        include = 0
        if wt[index]<=rem_weight:
            include = val[index] + helper(index+1, rem_weight-wt[index])
        dp[index][rem_weight]= max(exclude, include) #storing 
        return dp[index][rem_weight]
    return helper(0,W)

print(knapSack(8,[8,2,5],[2,3,9],3))