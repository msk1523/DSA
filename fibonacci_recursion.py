# Coding Exercise: Fibonacci
# Question:

# Fibonacci - In the Fibonacci sequence, each subsequent term is obtained by adding the preceding 2 terms. This is true for all the numbers except the first 2 numbers of the Fibonacci series as they do not have 2 preceding numbers. The first 2 terms in the Fibonacci series is 0 and 1. F(n) = F(n-1)+F(n-2) for n>1. Write a function that finds F(n) given n where n is an integer greater than equal to 0. For the first term n = 0. (You can assume that no negative value will be passed. )

# Try:

# Try to optimise your solution. We will be discussing 3 solutions

# Solution 1: T=O(2^n) , S=O(n)

# Solution 2: T=O(n) , S=O(n)

# Solution 3: T=O(n) , S=O(1) --- best

def fibonacci(n):
    if n<=1: return n
    else: return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))#55