""" 
931. Minimum Falling Path Sum 

Difficulty:  Medium
"""


class Solution:
    def minFallingPathSum(self,matrix: list[list[int]]) -> int:
        for i in range(1,len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] += min(matrix[i-1][j and j-1 : j+2])
                
        return min(matrix[-1])
    
    
def main():
    solution = Solution()
    
    # TesCase
    matrix = [[2,1,3],
              [6,5,4],
              [7,8,9]]
    
    result = solution.minFallingPathSum(matrix)
    print(result)
    
if __name__ == '__main__':
    main()