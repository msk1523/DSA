"""
LIS
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:

Input: nums = [300,9,2,5,3,7,500,400]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,500], 
therefore the length is 4.
"""

def lengthOfLIS(nums):
    
    n=len(nums)
    dp=[1]*n
    
    max=1 
    
    for i in range(1,n):
        for j in range(i):
            if nums[i]>nums[j] and dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1
        if dp[i]>max:
            max=dp[i]
    return max

print(lengthOfLIS([300,9,2,5,3,7,500,400]))