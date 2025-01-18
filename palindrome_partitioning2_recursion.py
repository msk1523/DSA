""" 
Palindrom Partitioning 2 ( Min Cuts)
Palindrom Partitioning 2 :

Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
Input: s = "ppq"
Output: 1
Explanation: The palindrome partitioning ["pp","q"] could be produced using 1 cut.
"""

def minCut(s):
    n = len(s)
    def isPalindrome(i,j):
        while i<j:
            if s[i] != s[j]: return False
            i+=1 
            j-=1 
        return True
        
    def partition(start,end):
        #base case 
        if start == end or isPalindrome(start,end):
            return 0
        
        #recursive case
        minimum = end-start
        for end_index in range(start,end):
            if isPalindrome(start,end_index):
                minimum = min(minimum,1+partition(end_index+1,end))
                
        return minimum
        
    return partition(0,n-1)

print(minCut("ppq"))