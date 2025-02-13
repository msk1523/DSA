""" 
Coding Exercise: Rotate Array
Question

Given an array, rotate the array to the right by k steps, where k is non-negative.



Try :

After you have solved this question, think about whether you can solve it in constant space
"""

def rotate(nums, k):
    n = len(nums)
    k = k % n  # In case k is greater than the length of the array

    # Helper function to reverse a portion of the array
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse the entire array
    reverse(0, n - 1)
    
    # Step 2: Reverse the first k elements
    reverse(0, k - 1)
    
    # Step 3: Reverse the remaining n-k elements
    reverse(k, n - 1)

# Example usage
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]