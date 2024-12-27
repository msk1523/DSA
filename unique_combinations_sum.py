# Coding Exercise: Combinations Sum 2
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

# Example :

# Input: candidates = [3,5,2,1,3], target = 7
# Output: 
# [
# [1,3,3],
# [5,2]
# ]

def combinationSum2(candidates, target):
    res = []
    candidates.sort()
    def backtrack(index,currSum,curr):
        if currSum == target:
            res.append(curr[:])
            return
        if currSum>target:
            return
        if index > len(candidates)-1:
            return
        hash = {}    
        for j in range(index,len(candidates)):
            if candidates[j] not in hash:
                hash[candidates[j]]=1
                curr.append(candidates[j])
                backtrack(j+1,currSum+candidates[j],curr)
                curr.pop()
    backtrack(0,0,[])
    return res                

print(combinationSum2([3,5,2,1,3],7))