# Coding Exercise ( Permutations)
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:

# nums = [1,4]

# Output :[[1,4],[4,1]]

# Example 2:

# nums = [1,4,5]

# Output :[[1,4,5],[1,5,4],[4,1,5],[4,5,1],[5,1,4],[5,4,1]]

def permute(nums):
    res = []
    n = len(nums)
    def helper(index):
        #base case
        if index == n-1:
            res.append(nums[:])
            return
        for i in range(index, n):
            #swap
            nums[index], nums[i] = nums[i], nums[index]
            #recursion
            helper(index+1)
            #backtrack
            nums[index], nums[i] = nums[i], nums[index]
    helper(0)
    return res

nums = [1,4,5]
permute(nums)