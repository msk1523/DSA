""" 
Russian Doll Envelopes

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.
One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.
Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).
Note: You cannot rotate an envelope.

Example :
Input: envelopes = [[6,5],[7,5],[7,8],[3,4]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([3,4] => [6,5] => [7,8]).
"""

def maxEnvelopes(envelopes):
    #Write code here
    n = len(envelopes)
    dp = [1]*n 
    envelopes.sort()
    longest_chain=1
    for i in range(1,n):
        for j in range(i):
            if envelopes[j][0]<envelopes[i][0] and envelopes[j][1]<envelopes[i][1]:
                if dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1 
        if dp[i]>longest_chain:
            longest_chain=dp[i]
    return longest_chain

print(maxEnvelopes([[6,5],[7,5],[7,8],[3,4]]))