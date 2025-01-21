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
    dp = [False]*n

    for i in range(n):
        for word in wordDict:
            if i<len(word)-1:
                continue
            elif s[i-len(word)+1:i+1]==word and (i==len(word)-1 or dp[i-len(word)]):
                dp[i]=True
                break
    return dp[n-1]              

print(wordBreak("jackson",["jack","son"]))