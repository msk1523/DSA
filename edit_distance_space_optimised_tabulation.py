"""Edit Distance
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

    prev=[0]*(m+1)
    curr=[0]*(m+1)

    for j in range(m+1):
        prev[j]=j 
    
    for i in range(1,n+1):
        curr[0]=i
        for j in range(1,m+1):
            if word1[i-1]==word2[j-1]:
                curr[j]=prev[j-1]
            else:
                replace = 1 + prev[j-1]
                delete = 1 + prev[j]
                insert = 1+ curr[j-1]
                curr[j] = min(delete,replace,insert)
        prev=curr[:]
    return prev[m]

print(minDistance("hodse","dos"))