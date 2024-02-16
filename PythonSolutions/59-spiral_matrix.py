from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        def dirToIndex(x, y, d):
            if d == 'r': return (x, y + 1, d) if y + 1 < n and matrix[x][y + 1] == 0 else (x + 1, y, 'd')
            elif d == 'd': return (x + 1, y, d) if x + 1 < n and matrix[x + 1][y] == 0 else (x, y - 1, 'l')
            elif d == 'l': return (x, y - 1, d) if y > 0 and matrix[x][y - 1] == 0 else (x - 1, y, 'u')
            else: return (x - 1, y, d) if x > 0 and matrix[x - 1][y] == 0 else (x, y + 1, 'r')
                      
        matrix = [[0 for i in range(1, n + 1)] for j in range(n)]

        num = 1
        dir = 'r'
        i = 0
        j = 0
        while 0 <= i < n and 0 <= j < n and matrix[i][j] == 0:
            matrix[i][j] = num
            num += 1
            i, j, dir = dirToIndex(i, j, dir)
        
        return matrix
    
    
solution = Solution()

# TestCase
n = 3
print(solution.generateMatrix(n)) #Expected: [[1,2,3],[8,9,4],[7,6,5]]