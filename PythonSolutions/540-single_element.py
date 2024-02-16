from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
            ## METHOD ONE

        # for i in range(0, len(nums), 2):
        #     if i + 1 < len(nums) and nums[i] != nums[i + 1]:
        #         return nums[i]
        # return nums[-1]

            ## METHOD TWO

        # l = 0
        # r = len(nums) - 1
        
        # while l <= r:
        #     mid = (l + r) // 2
            
        #     if mid == len(nums) - 1 or nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
        #         return nums[mid]
            
        #     if mid % 2 == 0:
        #         if nums[mid] == nums[mid + 1]:
        #             l = mid + 2
        #         else:
        #             r = mid - 2
        #     else:
        #         if nums[mid] == nums[mid - 1]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1


            ## METHOD THREE
            
        count = 0
        for i in nums:
            count ^= i
        return count
                
solution = Solution()

# TestCase
nums = [1,1,2,3,3,4,4,8,8]
print(solution.singleNonDuplicate(nums))