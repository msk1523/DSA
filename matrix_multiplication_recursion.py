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