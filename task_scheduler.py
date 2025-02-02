""" 
Task Scheduler
You are given an array of CPU tasks, each represented by letters A to Z, and a colling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there is a constraint: identical tasks must be  seperated by at least n intervals due to cooling time.
Return the minimum number of intervals required to complete all tasks.
"""

def leastInterval(tasks, n):
    
    count = [0]*26
    max_freq = 0
    number_max_freq = 0
    
    for task in tasks:
        index = ord(task) - ors('A') #ord function in python returns the unicode code 
        count[index] +=1 
        if max_freq < count[index]:
            max_freq = count[index]
            number_max_freq = 1
        elif max_freq == count[index]:
            number_max_freq +=1 
    parts = max_freq-1
    slots_per_part = n-(number_max_freq-1)
    total_slots_in_parts = parts* slots_per_part
    tasks_rem = len(tasks) - max_freq(number_max_freq)
    idles = max(0,total_slots_in_parts - tasks_rem)
    return len(tasks) + idles

print(leastInterval(['A','A','A','B','B','B'], 2))