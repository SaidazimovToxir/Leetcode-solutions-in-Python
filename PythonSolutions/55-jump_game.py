from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = maxx = 0
        
        while i < len(nums) and i <= maxx:
            if nums[i] + i >= len(nums) - 1:
                return True
            
            maxx = max(maxx, i + nums[i])
            
            i += 1
        
        return False
        
solution = Solution()

# TestCase

# nums = [2,3,1,1,4]
nums = [3,2,1,0,4]

print(solution.canJump(nums))