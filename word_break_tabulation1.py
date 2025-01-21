""" 
Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example :
Input: s = "jackson", wordDict = ["jack","son"]
Output: true
Explanation: Return true because "jackson" can be segmented as "jack son".
"""

def wordBreak(s, wordDict):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    for l in range(1,n+1):
        for i in range(n-l+1):
            j = i+l-1
            if s[i:j+1] in wordDict:
                dp[i][j]=True
            else:
                for k in range(i,j):
                    dp[i][j] = dp[i][j] or (dp[i][k] and dp[k+1][j])
    return dp[0][n-1]

print(wordBreak("jackson",["jack","son"]))