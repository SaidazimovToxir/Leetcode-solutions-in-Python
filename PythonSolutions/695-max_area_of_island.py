""" 
695. Max Area of Island

Difficulty: Medium
"""

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        seen = set()
        def area(r,c): # Use to Recurtion !!!
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r,c))

            return (1 + area(r+1, c) + area(r-1, c) + area(r, c-1) + area(r, c+1))

        return max(area(r,c)
            for r in range(len(grid))
            for c in range(len(grid[0]))
        )


def main():
    solution = Solution()
    
    # Testcase
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]] # expect 6
    
    result = solution.maxAreaOfIsland(grid)
    print(result)
    
if __name__ == '__main__':
    main()
    