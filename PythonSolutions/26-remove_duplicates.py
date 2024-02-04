""" 
26. Remove Duplicates from Sorted Array

Difficulty: Easy
"""


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[k] = (nums[i+1])
                k+=1

        return k
    
solution = Solution()
# TestCase

nums = [1,1,2] # expect 2, 1,2
print(solution.removeDuplicates(nums))