""" 
1. Two Sum
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    # numsHash = {}
    # for i in range(len(nums)):
    #     if target - nums[i] in numsHash:
    #         return [numsHash[target - nums[i]], i]
    #     numsHash[nums[i]] = i

    l = 0
    r = len(nums) - 1
    sort_nums = sorted(enumerate(nums), key=lambda x: x[1])
    
    while l < r:
        total = sort_nums[l][1] + sort_nums[r][1]
        print(sort_nums[r][1])
        
        if total < target: l += 1
        elif total > target: r -= 1
        else:
            print(sort_nums)
            return [sort_nums[l][0],sort_nums[r][0]]
            
nums1 = [2,7,11,15]
target1 = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3,3]
target3 = 6

twosum = twoSum(nums2,target2)
print(twosum)