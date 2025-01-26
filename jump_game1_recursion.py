""" 
Jump Game 1
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""

def can_jump_from_position(position, nums):
    if position == len(nums) - 1:
        return True

    furthest_jump = min(position + nums[position], len(nums) - 1)
    for next_position in range(position + 1, furthest_jump + 1):
        if can_jump_from_position(next_position, nums):
            return True

    return False

def can_jump(nums):
    return can_jump_from_position(0, nums)

print(can_jump([2,3,1,1,4]))