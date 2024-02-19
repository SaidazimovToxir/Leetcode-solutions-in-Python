from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse = True)
        s.sort(reverse = True)
        count = 0
        
        while s and g:
            if g[-1]  <= s[-1]: 
                count += 1 
                g.pop() 
                s.pop()
                
            else: 
                s.pop()
                
        return count
            
solution = Solution()

# Testcase

g = [1,2,3]; s = [1,1]

print(solution.findContentChildren(g,s))