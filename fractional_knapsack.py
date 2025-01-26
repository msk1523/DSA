""" 
Fractional Knapsack
Determine how to optimally fill a knapsack with a capacity of W kilograms using a list of N items, where each item is represented by a pair [profit, weight]. In the Fractional Knapsack problem, you can take fractions of items to maximize the total profit in the knapsack.(N will be greater than equal to 1 )

Example 1:

Given arr[] = [[70, 10], [90, 20], [150, 30]]
W= 25
Expected output = 145

Example 2:

Given arr[] = [[70, 10], [90, 20], [150, 30]]
W= 45
Expected output = 242.5
"""

def fractionalknapsack(W,arr,n):
    #sort arr by ratio of profit/weight
    
    arr.sort(reverse = True, key = lambda x:x[0]/x[1])
    
    remaining_weight = W 
    value = 0
    n = len(arr)
    
    for i in range(n):
        if remaining_weight == 0:
            break
        weight = min(remaining_weight, arr[i][1])
        remaining_weight -= weight
        value += arr[i][0]/arr[i][1] * weight
    return value

print(fractionalknapsack(25,[[70, 10], [90, 20], [150, 30]],3))