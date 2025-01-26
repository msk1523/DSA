""" 
Jump Game 1
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""

def canJump(nums):
    # Initialize the memoization table with None values
    memo = [None] * len(nums)
    memo[-1] = True  # The last index is always reachable from itself
    
    def canJumpFromPosition(position):
        if memo[position] is not None:
            # If we have already computed the value, return it
            return memo[position]

        # Compute the furthest jump from the current position
        furthestJump = min(position + nums[position], len(nums) - 1)
        
        # Check if any position reachable from here can reach the end
        for nextPosition in range(position + 1, furthestJump + 1):
            if canJumpFromPosition(nextPosition):
                memo[position] = True
                return True

        memo[position] = False
        return False

    # Start the recursive check from the first index
    return canJumpFromPosition(0)

print(canJump([2,3,1,1,4]))