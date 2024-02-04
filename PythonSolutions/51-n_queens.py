""" 
51. N-Queens

Difficulty: Hard
"""


from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def dfs(i, l, r, m, arr):
            if i == n:
                res.append(arr)
            else:
                l = l[1:] + [0]
                r = [0] + r[:-1]
                for j in range(n):
                    if m[j] == l[j] == r[j] == 0:
                        l[j] = r[j] = m[j] = 1 
                        dfs(i + 1, l, r, m, arr + [("." * j) + "Q" + ("." * (n - j - 1))])
                        l[j] = r[j] = m[j] = 0
        dfs(0, [0] * n, [0] * n, [0] * n, [])
        return res
    
solution = Solution()

# TestCase
n = 4 
print(solution.solveNQueens(n)) # Expected [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]