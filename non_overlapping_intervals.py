""" 
Non overlapping Intervals
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example:

[[1, 4], [2, 5], [5, 6], [3, 4]]

Output: In this example, removing [2, 5] and [3, 4] is sufficient. Thus, the answer is 2.
"""

def eraseOverlapIntervals(intervals):
    n = len(intervals)
    popped = 0
    intervals.sort()
    j=0
    for i in range(1,n):
        if i>j:
            if intervals[j][1] > intervals[i][0]:
                popped+=1 
            else: j=i+1
    return popped

print(eraseOverlapIntervals([[1, 4], [2, 5], [5, 6], [3, 4]]))