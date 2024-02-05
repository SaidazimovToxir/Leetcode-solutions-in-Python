""" 
462. Minimum Moves to Equal Array Elements II

Difficulty: Medium
"""



class Solution:
    def minMoves2(self, nums):
        nums.sort()
        m = nums[(len(nums) - 1) // 2] 
        return sum(abs(num - m) for num in nums)
    


solution = Solution()

# TestCase
nums = [1,2,3]
print(solution.minMoves2(nums))

