import itertools

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        p = itertools.permutations(range(1, n + 1))
        for i in range(k): 
            res = next(p)
        return ''.join([str(i) for i in res])
    
solution = Solution()

# TestCase

n = 3; k = 3

print(solution.getPermutation(n,k))