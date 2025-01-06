# Tribonacci
# The Tribonacci sequence Tn is defined as follows:

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn

def tribonacci(n):
    zero = 0
    one = 1
    two = 1
    if n<=1: return n
    if n==2: return two
    for i in range(3,n+1):
        next = zero + one+ two
        zero = one
        one = two
        two = next
    return next    

print(tribonacci(4))#4