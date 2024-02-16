from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        dp = [[0] * (len(nums2) + 1) for i in range(len(nums1) + 1)]
        
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    result = max(result, dp[i][j])
                    
        return result
    
solution = Solution()

# TestCase
nums1 = [1,2,3,2,1]; nums2 = [3,2,1,4,7]
print(solution.findLength(nums1,nums2))