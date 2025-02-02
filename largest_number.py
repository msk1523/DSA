""" 
Largest Number
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:

Input: nums = [10,2]
Output: "210"
"""

from functools import cmp_to_key

def largestNumber(nums):
    nums = list(map(str, nums))
    
    def compare(a, b):
        if a + b > b + a:
            return -1 
        else:
            return 1  
    nums.sort(key=cmp_to_key(compare))
    
    if nums[0] == '0':
        return '0'
    
    return ''.join(nums)

print(largestNumber([10,2]))