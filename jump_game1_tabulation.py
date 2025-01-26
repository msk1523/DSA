""" 
Jump Game 1
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""

def can_jump(nums):
    n = len(nums)
    # Create a DP table, initialized to False except the first element
    dp = [False] * n
    dp[0] = True  # Start is always reachable from itself

    # Fill the DP table from left to right
    for i in range(n):
        if dp[i]:  # If current index is reachable
            # Calculate the furthest we can reach from here
            furthest = min(i + nums[i], n - 1)
            # Mark all reachable positions as True
            for j in range(i + 1, furthest + 1):
                dp[j] = True

    # If the last position is True, then it's reachable
    return dp[-1]

print(can_jump([2,3,1,1,4]))