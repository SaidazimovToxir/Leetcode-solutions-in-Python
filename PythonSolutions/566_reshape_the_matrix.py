from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        lst = [x for y in mat for x in y]
        # print(lst)
        print(len(mat))
        
        if r * c == len(mat) * len(mat[0]):
            return [lst[c * i : c * (i+1)] for i in range(r)]
        
        else:
            return mat
            

        
        
solution = Solution()

# TestCase
mat = [[1,2],[3,4]]; r = 1; c = 4
# mat = [[1,2],[3,4]]; r = 2; c = 4

print(solution.matrixReshape(mat,r,c))