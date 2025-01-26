""" 
Jump Game 1
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""

def canJump(nums):
    
    n = len(nums)
    max_index = 0
    
    for i in range(n):
        if i>max_index:
            return False
        max_index = max(max_index,i+nums[i])
        if max_index >= n-1:
            return True
    #return False

print(canJump([2,3,1,1,4]))