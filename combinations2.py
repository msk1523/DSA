# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

# Example:

# n = 4

# k=2

# Output =

# [

# [1,2],[1,3],[1,4],

# [2,3],[2,4],

# [3,4]

# ]


def combine(n,k):
    res=[]
    def helper(start,curr):
        if len(curr)==k:
            res.append(curr[:])
            return
        need=k-len(curr)
        for j in range(start,n-(need-1)+1):
            curr.append(j)
            helper(j+1,curr)
            curr.pop()
    helper(1,[])
    return res

print(combine(4,2))
# [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]