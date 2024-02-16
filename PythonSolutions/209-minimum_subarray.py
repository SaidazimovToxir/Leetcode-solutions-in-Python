from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j = 0
        total = 0
        minsize = 0
            
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                if minsize == 0 or minsize > i - j + 1:
                    minsize = i - j + 1
                total -= nums[j]
                j += 1
                
        return minsize

solution = Solution()

# TestCase
target = 12; nums = [6,6,12]


print(solution.minSubArrayLen(target, nums))
