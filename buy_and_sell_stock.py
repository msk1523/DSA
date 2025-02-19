""" 
Coding Exercise: Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example:
Input: prices = [9,1,5,3,7,5]
Output: 6
"""

def maxProfit(prices):
    left = 0
    profit = 0
    for right in range(1,len(prices)):
        if prices[right] < prices[left]:
            left = right
        else:
            profit = max(profit,prices[right]-prices[left])    
    return profit

print(maxProfit([9,1,5,3,7,5]))