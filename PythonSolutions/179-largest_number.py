from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = ''.join(map(str, nums))
        m = ''.join(map(str, n))
        return sorted(m, reverse=True)        
        
        
        
        
solution = Solution()

nums = [3,30,34,5,9]
print(solution.largestNumber(nums))