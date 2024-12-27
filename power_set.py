
# Subsets
# Question:

# Power Set - Given an integer array of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

def power_set (nums):
    output = []
    def helper (nums,i,subset):
        if i == len(nums):
            output.append(subset.copy())
            return
        helper(nums,i+1,subset) #no of iterations
        subset.append(nums[i])
        helper(nums,i+1,subset)
        subset.pop()
    helper(nums,0,[])
    return output

out=power_set([1,2,3]) # [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
print(out)