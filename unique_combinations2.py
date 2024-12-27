# Coding Exercise: Combinations Sum 3
# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

# Only numbers 1 through 9 are used.

# Each number is used at most once.

# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

# Example :

# Input: k = 3, n = 6
# Output: [[1,2,3]] 
# Explanation:
# 1 + 2 + 3 = 6
# There are no other valid combinations.

def combinationSum3(k, n):
    res = []
    def backtrack(number,curr,currSum):
        if currSum ==n and len(curr)==k:
            res.append(curr[:])
            return
        if currSum >n or len(curr)==k:
            return
        for x in range(number,10):
            curr.append(x)
            backtrack(x+1,curr,currSum+x)
            curr.pop()
    backtrack(1,[],0)
    return res                

print(combinationSum3(3,6))