""" 
3 Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Example:
Input: nums = [-2,0,2,1,-1,-3]
Output: [[-2,0,2],[0,1,-1],[2,1,-3]]
Input: nums = [-1,2,6,-1,1]
Output: [[-1,2,-1]]
"""

def threeSum(nums):
    res=set()
    for i in range(len(nums)):
        need=set()
        for j in range(i+1,len(nums)):
            valueNeeded = -(nums[i]+nums[j])
            if valueNeeded in need:
                triplet=tuple(sorted(nums[i], nums[j], valueNeeded))
                res.add(triplet)
            need.add(nums[j])
    return list((triplet) for triplet in res)

print(threeSum([-2,0,2,1,-1,-3]))