from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in nums:
            for j in nums:
                if j - i == k:
                    count += 1

        return count
    
    
solution = Solution()
nums = [3,2,1,5,4]
k = 2

print(solution.countKDifference(nums,k))