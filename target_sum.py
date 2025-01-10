"""
Target Sum
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.

Example 1:

Input: nums = [1,1,1,1], target = 2
Output: 4
Explanation: There are 4 ways to assign symbols to make the sum of nums be target 2.
-1 + 1 + 1 + 1  = 2
+1 - 1 + 1 + 1  = 2
+1 + 1 - 1 + 1  = 2
+1 + 1 + 1 - 1  = 2

"""

def findTargetSumWays(nums, target):
    n = len(nums)
    summation = sum(nums)
    dp = [[None]*(2*summation+1) for _ in range(n)]

    def helper(index,sum_nums):
        #base case
        if index<0:
            if sum_nums==target:return 1
            else:return 0
        if dp[index][sum_nums+summation]!=None:return dp[index][sum_nums+summation]

        negative = helper(index-1,sum_nums+-1*nums[index])
        positive = helper(index-1,sum_nums+nums[index])    
        dp[index][sum_nums+summation] = negative+positive
        return dp[index][sum_nums+summation]
    return helper(n-1,0) 

print(findTargetSumWays([1,1,1,1],2))