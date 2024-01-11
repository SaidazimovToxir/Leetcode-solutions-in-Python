def twoSum(nums: list[int], target: int) -> list[int]:
    numsHash = {}
    for i in range(len(nums)):
        if target - nums[i] in numsHash:
            return [numsHash[target - nums[i]], i]
        numsHash[nums[i]] = i
            
nums1 = [2,7,11,15]
target1 = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3,3]
target3 = 6

twosum = twoSum(nums2,target2)
print(twosum)