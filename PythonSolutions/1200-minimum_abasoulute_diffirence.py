from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        
        lst = min(b - a for a, b in zip(arr, arr[1:]))
        return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == lst]
        
        
solution = Solution()

# TestCase
arr = [4,2,1,3]

print(solution.minimumAbsDifference(arr))