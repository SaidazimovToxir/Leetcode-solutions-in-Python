class Solution:
    def findNumberOfLIS(self, nums):
        lst = [[1, 1] for i in range(len(nums))]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    if lst[i][0] >= lst[j][0]: lst[j] = [lst[i][0] + 1, lst[i][1]]
                    elif lst[i][0] == lst[j][0] - 1: lst[j][1] += lst[i][1]
        lst.sort()
        return lst and sum(d[1] for d in lst if d[0] == lst[-1][0]) or 0
    
    
solution = Solution()

# TestCase

nums = [1,3,5,4,7]

print(solution.findNumberOfLIS(nums))