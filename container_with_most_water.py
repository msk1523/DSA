""" 
Coding Exercise: Container with most water
Question
Container with most Water - You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of 
the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the 
most water(depth is constant across containers). Return the area(that the 2 lines and the X axis make) of container which can store the max 
amount of water. Notice that you may not slant the container.

Try:
To optimise your solution . In case you approached this question with the Brute force method your Time Complexity might be O(n^2).
Try to write a better solution with Time Complexity O(n)
"""

def max_area(height):
    n = len(height)
    left = 0
    right = n - 1
    max_area = 0

    while left < right:
        height_left = height[left]
        height_right = height[right]
        height_min = min(height_left, height_right)
        width = right - left
        area = height_min * width
        max_area = max(max_area, area)
        if height_left < height_right:
            left += 1
        else:
            right -= 1

    return max_area

print(max_area([1,8,6,2,5,4,8,3,7]))
