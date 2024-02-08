from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:    
            # Time complexity: O(log n), Memory complexity O(1)

        # l = 0
        # r = len(nums) - 1
        # while l <= r:
        #     mid = (l + r) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif sum((target < nums[l], nums[l] <= nums[mid], nums[mid] < target)) == 2:
        #         l = mid + 1
        #     else: r = mid - 1
        # return -1


            # Time complexity: O(n), Memory complexity: O(1)
            
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
    
solution = Solution()

# TestCase

nums = [4,5,6,7,0,1,2]
target = 0

print(solution.search(nums,target)) # Expected: 4