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
    dp=[[0]*(n+1) for _ in range(n+1)]
    
    for i in range (n-1,-1,-1):
        for j in range(i,-1,-1):
            exclude = dp[i+1][j]
            include = 0
            if j-1 == -1 or nums[i]>nums[j-1]:
                include = 1+ dp[i+1][i+1]
            dp[i][j] = max(exclude,include)
    return dp[0][0]

print(lengthOfLIS([300,9,2,5,3,7,500,400]))