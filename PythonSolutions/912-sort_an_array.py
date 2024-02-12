import random

def sortArray(nums):
    if len(nums) <= 1:
        return nums
    
    pivot = random.choice(nums)
    r = [v for v in nums if v < pivot]
    eq = [v for v in nums if v == pivot]
    l = [v for v in nums if v > pivot]
    
    return sortArray(r) + eq + sortArray(l)

n = [5,2,3,1]
print(sortArray(n))