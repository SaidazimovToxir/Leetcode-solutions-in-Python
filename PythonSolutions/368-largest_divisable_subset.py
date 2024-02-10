from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        lst = [[i] for i in sorted(nums)]
        
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if not lst[j][-1] % lst[i][-1] and len(lst[i]) >= len(lst[j]):
                    lst[j] = lst[i] + lst[j][-1:]
                    # print(lst)
                    
        return  lst and sorted(lst, key=len)[-1] # "key=len" -> har bir uzunlik bo'yicha sortlash, Listdagi eng uzun elementni topish uchun     
        
solution = Solution()

# TestCase

nums = [2,3,4,9,8]
print(solution.largestDivisibleSubset(nums)) # Expected: [2,4,8]
