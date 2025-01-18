""" 
Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:

Input: s = "ppq"
Output: [["p","p","q"],["pp","q"]]
"""

def partition(s):
    n = len(s)
    dp=[[0]*n for _ in range(n)]

    for l in range(1,n+1):
        for i in range(0,n-l+1):
            j=i+l-1
            if i==j: dp[i][j]=True
            elif s[i]==s[j] and (j==i+1 or dp[i+1][j-1]):
                dp[i][j]=True
            else:dp[i][j]=False

    def helper(index,curr):
        #base case
        if index>n-1:
            res.append(curr[:])
            return 
        for i in range(index,n):
            if dp[index][i]:
                curr.append(s[index:i+1])
                helper(i+1,curr)
                curr.pop()
    res = []
    helper(0,[])            
    return res            

print(partition("ppq"))