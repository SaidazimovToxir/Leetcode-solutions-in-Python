from typing import List

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        x, y = 0, 0
        rows, cols = len(matrix), len(matrix[0])
        result = [0] * (rows * cols)

        for i in range(rows * cols):
            result[i] = matrix[x][y]
            # print(result)

            if (x + y) % 2 == 0:
                if y == cols - 1:
                    x += 1
                elif x == 0:
                    y += 1
                else:
                    x -= 1
                    y += 1
            else:
                if x == rows - 1:
                    y += 1
                elif y == 0:
                    x += 1
                else:
                    x += 1
                    y -= 1

        return result
        
        
        
solution = Solution()

# TestCase
mat = [[1,2,3],[4,5,6],[7,8,9]]
# mat = [[2,3]]
# mat = [[2],[3]]

print(solution.findDiagonalOrder(mat))