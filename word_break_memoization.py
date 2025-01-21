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
    dp = [-1]*n 
    
    def check_ending_at(index):
        #base case 
        if index<0: return True
        if dp[index] != -1: return dp[index]
        
        #recursive case
        for word in wordDict:
            if s[index-len(word)+1:index+1] == word and check_ending_at(index-len(word)):
                dp[index]=True
                return dp[index]
        dp[index]=False
        return dp[index]
        
        
    return check_ending_at(n-1)

print(wordBreak("jackson",["jack","son"]))