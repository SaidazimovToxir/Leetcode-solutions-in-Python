from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        unique_nums = sorted(frequency.keys(), key=lambda x: frequency[x], reverse=True)
        
        return unique_nums[:k]
        
    

solution = Solution()

# TestCase
nums = [1,1,1,2,2,3]; k = 2

print(solution.topKFrequent(nums,k))
