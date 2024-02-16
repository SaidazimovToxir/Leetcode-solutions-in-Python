from typing import List

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # d = abs(target[0]) + abs(target[1])
        # for ghost in ghosts:
        #     if abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) <= d: return False
        # return True
        d = target[0] + target[1]
        
        for i in ghosts:
            print(i[0] - target[0] + i[1] - target[1])
            if i[0] - target[0] + abs(i[1] - target[1]) <= d: return False
        return True


solution = Solution()

# TestCase
ghosts = [[1,0],[0,3]]; target = [0,1]

print(solution.escapeGhosts(ghosts,target))