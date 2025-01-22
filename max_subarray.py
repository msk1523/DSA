""" 
Max Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example :

Input: nums = [1,2,-10,3,9]
Output: 12
Explanation: The subarray [3,9] has the largest sum 12.
"""

def maxSubArray(nums):
    n = len(nums)
    max_sum = -float('inf')
    sum_curr_subarray_considered = 0

    for num in nums:
        sum_curr_subarray_considered += num
        if sum_curr_subarray_considered>max_sum:
            max_sum = sum_curr_subarray_considered
        if sum_curr_subarray_considered <0:
            sum_curr_subarray_considered = 0
    return max_sum 

print(maxSubArray([1,2,-10,3,9]))