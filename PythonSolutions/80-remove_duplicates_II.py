""" 
80. Remove Duplicates from Sorted Array II

Difficulty: Medium
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2
        for i in range(2, len(nums)):
            if nums[k-2]!=nums[i]:
                nums[k] = nums[i]
                k+=1

        return min(k,len(nums))
    
solution = Solution()

# TestCase
nums = [1,1,1,2,2,3] # Expect 5, [1,1,2,2,3,_]
print(solution.removeDuplicates(nums))