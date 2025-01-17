""" 
Palindromic Substrings
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "pqrp"
Output: 4
Explanation: Three palindromic strings: "p", "q", "r","p".
"""
def countSubstrings(s):
    res = 0
    n = len(s)

    dp = [[0]*n for _ in range(n)]

    for l in range(1,n+1):
        for i in range(n-l+1):
            j = i+l - 1
            if i==j: 
                dp[i][j] = True
                res+=1
            elif s[i]==s[j] and (j==i+1 or dp[i+1][j-1]):
                dp[i][j] = True
                res +=1
            else:
                dp[i][j] = False
    return res

print(countSubstrings("pqprps"))