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
    isPalindrome = [[0]*n for _ in range(n)]
    for l in range(1,n+1):
        for i in range(n-l+1):
            j = i+l-1
            if i == j: isPalindrome[i][j] = True
            elif s[i] == s[j] and (j == i+1 or isPalindrome[i+1][j-1]):
                isPalindrome[i][j] = True
            else:
                isPalindrome[i][j] = False
    dp = [[None]*n for _ in range(n)]
    
    def partition(start,end):
        #base case 
        if start == end or isPalindrome[start][end]:
            return 0
        
        #recursive case
        if dp[start][end] is not None:
            return dp[start][end]
        minimum = end-start
        for end_index in range(start,end):
            if isPalindrome[start][end_index]:
                minimum = min(minimum,1+partition(end_index+1,end))
        dp[start][end] = minimum       
        return dp[start][end]
        
    return partition(0,n-1)

print(minCut("ppq"))