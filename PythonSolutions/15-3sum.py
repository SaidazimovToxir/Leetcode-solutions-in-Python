from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        res_set = set()
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                # print("s -> ",s)
                
                if s < 0: l += 1
                elif s > 0: r -= 1
                elif (nums[i], nums[l], nums[r]) not in res_set:
                    res.append([nums[i], nums[l], nums[r]])
                    res_set.add((nums[i], nums[l], nums[r]))
                    # print(nums[i],nums[l],nums[r]) 
                    # print(res)
                    
                else:
                    l += 1
                    r -= 1
        return res

solution = Solution()

# TestCase
nums = [-1,0,1,2,-1,-4]

print(solution.threeSum(nums)) # Expected: [[-1,-1,2],[-1,0,1]]