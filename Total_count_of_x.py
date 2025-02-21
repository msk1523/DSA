""" 
Given a number n, we define two functions:
1. The first function, sum(n), represents the sum of all the integers from 0 to n, calculated as 0 + 1 + 2 + 3 + ... + n.
2. The second function, xorSum(n,x), represents the sum of the bitwise XOR operation applied between each number from 0 to n and a given number x, meaning (0 ⊕ x) + (1 ⊕ x) + (2 ⊕ x) + ... + (n ⊕ x).
Here, x can take any value from 0 to n(inclusive).

The task is to return the sum of all such x satisfying the equation sum(n) = xorSum(n,x).
"""

class Solution:
    def sum_n(self, n):
        return n * (n + 1) // 2

    def xor_sum(self, n, x):
        result = 0
        for i in range(n + 1):
            result += i ^ x
        return result

    def totalCount(self, n):
        target_sum = self.sum_n(n)
        valid_x_sum = 0
        
        for x in range(n + 1):
            if self.xor_sum(n, x) == target_sum:
                valid_x_sum += x
        
        return valid_x_sum
    
print(Solution().totalCount(5))