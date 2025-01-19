""" 
Palindrom Partitioning 2 ( Min Cuts)
Palindrom Partitioning 2 :

Given a string s, partition s such that every substring of the partition is a palindrome. Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
Input: s = "ppq"
Output: 1
Explanation: The palindrome partitioning ["pp","q"] could be produced using 1 cut.
"""

def minCut(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]

    for l in range(1,n+1):
        for i in range(0,n-l+1):
            j=i+l-1
            if i==j:dp[i][j]=0
            elif s[i]==s[j] and (dp[i+1][j-1]==0):
                dp[i][j]=0
            else:
                dp[i][j]=j-i
                for k in range(i,j):
                    dp[i][j]=min(dp[i][j],1+dp[i][k]+dp[k+1][j])
    return dp[0][n-1]                

print(minCut("abaac"))