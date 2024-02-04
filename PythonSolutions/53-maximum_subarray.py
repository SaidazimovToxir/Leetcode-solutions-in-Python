""" 
53. Maximum Subarray

Difficulty: Medium
"""


class Solution:
    def maxSubArray(self, nums):
        s = 0
        m = 0
        n = -float("inf")
        for num in nums:
            s += num
            n = max(n, s - m)
            m = min(m, s)
        return n
    
    
solution = Solution()

# TestCase
nums = [-2,1,-3,4,-1,2,1,-5,4] 
print(solution.maxSubArray(nums)) # Expected 6
