""" 
Boats to Save people
You are given an array people where people[i] is the weight of the ith person, 
and an infinite number of boats where each boat can carry a maximum weight of limit. 
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.

Input: people = [3, 5, 2, 4], limit = 5

Output: 3

1 boat for Person 1 and Person 3.

1 boat for Person 2.

1 boat for Person 4.
"""

def numRescueBoats(people, limit):
    people.sort()  
    left, right = 0, len(people) - 1
    boats = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1 
        right -= 1
        boats += 1 
    
    return boats

print(numRescueBoats([3, 5, 2, 4], 5))