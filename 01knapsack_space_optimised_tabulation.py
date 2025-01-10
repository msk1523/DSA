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
    #write code here
    prev = [0]*(W+1)
    curr = [0]*(W+1)
    for i in range(1, n+1):
        for j in range (1, W+1):
            exclude = prev[j]
            include = 0
            if wt[i-1]<=j:
                include = val[i-1]+prev[j-wt[i-1]]
            curr[j] = max(exclude, include)
        prev = curr[:]
    return curr[W]

print(knapSack(8,[8,2,5],[2,3,9],3))