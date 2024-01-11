class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHash = {}
        for i in range(len(nums)):
            if target - nums[i] in numsHash:
                return [numsHash[target - nums[i]], i]
            numsHash[nums[i]] = i