""" 
Two City Scheduling
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], 
the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
"""

def twoCitySchedCost(costs):
    def minCost(i, a_count):
        # Base case: when all people have been considered
        if i == len(costs):
            # Base case: if we've considered all people, we wil have sent exactly n to A. 
            #so we can just return 0. There is no need to again check whether n people 
            #are sent to city A
            return 0

        # Cost of sending the i-th person to City A
        if a_count < len(costs) // 2:
            costA = costs[i][0] + minCost(i + 1, a_count + 1)
        else:
            costA = float('inf')  # Prevent sending more than n people to City A
        
        # Cost of sending the i-th person to City B
        b_count = i - a_count  # Number of people sent to City B so far
        if b_count < len(costs) // 2:
            costB = costs[i][1] + minCost(i + 1, a_count)
        else:
            costB = float('inf')  # Prevent sending more than n people to City B

        # Return the minimum cost of the two choices
        return min(costA, costB)

    # Start the recursion from the 0-th index with 0 people sent to A
    return minCost(0, 0)

print(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])) # 110