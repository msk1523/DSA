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
    n = len(nums)
    result = []
    nums.sort()

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result

print(threeSum([-2,0,2,1,-1,-3]))