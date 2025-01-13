"""
Edit Distance
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

•Insert a character

•Delete a character

•Replace a character

Example:

Input: word1 = "hodse", word2 = "dos"
Output: 3
Explanation: 
hodse -> dodse (replace 'h' with 'd')
dodse -> dose (remove 'd')
dose -> dos (remove 'e')
"""

def minDistance(word1, word2):
    
    n = len(word1)
    m = len(word2)
    
    dp=[[-1]*m for _ in range(n)]
    
    def helper(index1,index2):
        #base case 
        if index1>n-1 and index2>m-1:
            return 0
        if index1>n-1:
            return m-index2
        if index2>m-1:
            return n-index1
        
        if dp[index1][index2]!=-1:
            return dp[index1][index2]
        #recursive case
        if word1[index1]==word2[index2]:
            dp[index1][index2]=helper(index1+1,index2+1)
        else:
            replace=1+helper(index1+1,index2+1)
            delete=1+helper(index1+1,index2)
            insert=1+helper(index1,index2+1)
            dp[index1][index2]= min(replace,delete,insert)
        return dp[index1][index2]
        
    return helper(0,0)

print(minDistance("hodse","dos"))