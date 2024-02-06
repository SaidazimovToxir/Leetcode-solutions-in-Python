from typing import List


class Solution:
    def cobine(self, n: int, k: int) -> List[List[int]]:
        b = [[]]
        for i in range(1,n+1):
            b += [arr + [i] for arr in b if len(arr) < k]
        return [arr for arr in b if len(arr) == k]
    
solution = Solution()

# TestCase
n = 4
k = 2
print(solution.cobine(n,k)) # Expected: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]