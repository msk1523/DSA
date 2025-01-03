# Coding Exercise: Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# n>=1

# Example

# Input: n = 2
# Output: 2
# Explanation: You can climb to the top in 2 ways.
# A. 1 step + 1 step
# B. 2 steps

def climbStairs(n):
    if n<=2: return n
    def helper(first,second,n,curr):
        #subproblem
        #base condition
        next = first + second
        if curr==n: return next
        return helper(second,next,n,curr+1)
    return helper(1,2,n,3)

print(climbStairs(4))#5