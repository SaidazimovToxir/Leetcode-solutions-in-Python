# from typing import List

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         result = [0] * len(temperatures)
#         lst = []
        
#         for i in range(len(temperatures)):
#             while lst and temperatures[i] > temperatures[lst[-1]]:
#                 # print(lst[-1])
#                 n = lst.pop()
#                 # print(n)
#                 result[n] = i - n
            
#             lst.append(i)
#             print(lst)
        
#         return result
        
# solution = Solution()

# # TestCase
# temperatures = [73,74,75,71,69,72,76,73]

# print(solution.dailyTemperatures(temperatures))

# n = [1,2,3,4,5,6,7,8,9,10]
import random

a = int(input("List uzunligini kiriting: "))

n = [random.randint(1,a) for i in range(a)]
print(n)

count = 0

res = []

for i in n:
    count += i
    res.append(count)
    
print(','.join(map(str, res)))