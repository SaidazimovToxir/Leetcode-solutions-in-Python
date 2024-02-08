from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums) Time complexity O(n)
        
        # min_arr = nums[0] # Time complexity O(n)
        # for i in nums[1:]:
        #     if i < min_arr:
        #         min_arr = i

        # return min_arr
        
        start = 0
        end = len(nums)-1
        mid = (start+end)//2
        if not nums:
            return
        if start == end:
            return nums[0]
        
        if nums[start] > nums[end] and nums[mid] >= nums[start]:
            return self.findMin(nums[mid+1:end+1])
        
        else:
            return self.findMin(nums[start:mid+1])
        
solution = Solution()

# TestCase

nums = [3,4,5,1,2]

print(solution.findMin(nums)) # Expected: 1