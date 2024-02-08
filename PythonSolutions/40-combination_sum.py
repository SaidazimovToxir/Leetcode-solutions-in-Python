from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(sorted(candidates), target, 0, [], res)
        return res
    def dfs(self, nums, target, index, path, res):    
        if target < 0:
            return 
        if target == 0 and path not in res:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            if i>1 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i] + nums[i+1:], target-nums[i], i, path+[nums[i]], res)


solution = Solution()

# TestCase
candidates = [10,1,2,7,6,1,5]
target = 8

print(solution.combinationSum2(candidates,target)) # Expexted: [[1,1,6],[1,2,5],[1,7],[2,6]]