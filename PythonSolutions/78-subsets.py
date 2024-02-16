from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            # print([j+[i] for j in res])
            res += [j+[i] for j in res]

        return res            
solution = Solution()

# TestCase
nums = [1,2,3]
print(solution.subsets(nums))