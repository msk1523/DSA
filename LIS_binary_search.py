"""
LIS
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:

Input: nums = [300,9,2,5,3,7,500,400]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,500], 
therefore the length is 4.
"""
#binary search will give us a better time complexity than the tabulation approach and other sorting approaches

def lengthOfLIS(nums):
    
    def binarySearch(sub,num):
        left,right = 0,len(sub)-1
        while left < right:
            mid = (left+right)//2
            if sub[mid] < num:
                left = mid+1
            else:
                right = mid
        return left
        
    sub = [nums[0]]
    n = len(nums)
    
    for num in nums[1:]:
        if num>sub[-1]:
            sub.append(num)
        else:
            index = binarySearch(sub,num)
            #index - least value in sub >=num
            sub[index] = num
    return len(sub)

print(lengthOfLIS([300,9,2,5,3,7,500,400]))