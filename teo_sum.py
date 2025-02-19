""" 
Coding Exercise: Two Sum
Question:
Two Sum - You are given an array of Integers and another integer targetValue. 
Write a function that will take these inputs and return the indices of the 2 integers in the array that add up targetValue.

Try:
Try to optimise your solution and arrive at a Time Complexity of O(n)
Check the Hints section to get a clue

All the best. Keep at it !
"""

def two_sum(array,target):
    num_available = {}
    for i in range(len(array)):
        needed_val = target - array[i]
        if needed_val in num_available:
            return [i,num_available[needed_val]]
        else:
            num_available[array[i]]=i
    return []

print(two_sum([2,7,11,15],4))