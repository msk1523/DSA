""" 
Maximum Product Subarray
Given an integer array nums, find a subarray that has the largest product, and return the product.

Example :
Input: nums = [3,3,-2,4]
Output: 9
Explanation: [3,3] has the largest product 9.
"""

def maxProduct(nums):
    if not nums:
        return 0

    max_product = min_product = result = nums[0]

    for num in nums[1:]:
        if num < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)

        result = max(result, max_product)

    return result

print(maxProduct([3,3,-2,4]))