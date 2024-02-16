# import random

# def sortArray(nums):
#     if len(nums) <= 1:
#         return nums
    
#     pivot = random.choice(nums)
#     r = [v for v in nums if v < pivot]
#     eq = [v for v in nums if v == pivot]
#     l = [v for v in nums if v > pivot]
    
#     return sortArray(r) + eq + sortArray(l)

# n = [5,2,3,1]
# print(sortArray(n))

import math
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    left = 1
    right = 1
    for i in range(len(nums)):
        if i != 0:
            left = math.prod(nums[:i])
        if i != len(nums) - 1:
            right = math.prod(nums[i + 1:])
        nums[i] = left * right
    return nums

print(productExceptSelf([1, 2, 3, 4]))