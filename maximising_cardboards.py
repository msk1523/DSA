""" 
You are given an array arr[] representing side lengths of cardboard. 
Each length can be used at most once. You need to follow the following steps:
1. First maximise the number of square-based cardboards, each requiring 4 equal side lengths. 
2. After performing first step, maximise the number of rectangular-based cardboards from the remaining pieces, each requiring 2 pairs of equal side lengths.

Return the absolute difference between the number of square-based cardboards and rectangular-based cardboards you can make from arr[].
"""

class Solution:
    def cardboards(self, arr):
        # code here
        count={}
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        squares = 0
        rectangles = 0
        
        for key in count:
            squares += count[key] // 4
            count[key] %= 4
        
        pairs = 0
        for key in count:
            pairs += count[key] // 2
        
        rectangles = pairs // 2
        
        return abs(squares - rectangles)
    
print(Solution().cardboards([1,2,2,1,3,4,3,4]))