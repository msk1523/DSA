""" 
Matrix Chain Multiplication
Given a sequence of matrices, find the most efficient way to multiply these matrices together. The efficient way is the one that involves the least number of multiplications.
The dimensions of the matrices are given in an array arr[] of size N (such that N = number of matrices + 1) where the ith matrix has the dimensions (arr[i-1] x arr[i]).

Example:
Input: N = 4
arr = [2, 4, 6, 7]
Output: 132
Explanation: The matrices have dimensions (2*4),(4*6),(6*7)

If we multiply the first two first, the number of multiplications needed are 48 +84=132

If we multiply the last two first, the number of multiplications needed are 168+56=224
"""
def matrixMultiplication(N, arr):
    
    def findCost(i,j):
        #base case 
        if i == j:
            return 0
        
        #recursive case
        cost=float('inf')
        for k in range(i,j):
            curr_cost = findCost(i,k) + findCost(k+1,j) + arr[i-1]*arr[k]*arr[j]
            cost = min(cost,curr_cost)
        return cost
        
    return findCost(1,N-1)
    
print(matrixMultiplication(4,[2, 4, 6, 7]))