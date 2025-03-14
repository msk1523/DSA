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
    dp=[[-1]*n for _ in range(n)]
    def helper(curr_index,prev_index):
        #base case 
        if curr_index>n-1:
            return 0
        if dp[curr_index][prev_index+1]!=-1:
            return dp[curr_index][prev_index+1]
        #recursive case 
        exclude = helper(curr_index+1,prev_index)
        include = 0
        if prev_index == -1 or nums[curr_index]>nums[prev_index]:
            include = 1+helper(curr_index+1,curr_index)
        dp[curr_index][prev_index+1] = max(exclude,include)
        return dp[curr_index][prev_index+1]
        
    return helper(0,-1)

print(lengthOfLIS([300,9,2,5,3,7,500,400]))