""" 
Coding Exercise: Rotate Array
Question

Given an array, rotate the array to the right by k steps, where k is non-negative.
"""

def rotate_array(array,k):
    n=len(array)
    array1=[0]*n
    for i in range(n):
        j=(i+k)%n 
        array1[j]=array[i]
    array = array1
    return array

print(rotate_array([1,2,3,4,5,6,7],3))
print(rotate_array([-1,-100,3,99],2))