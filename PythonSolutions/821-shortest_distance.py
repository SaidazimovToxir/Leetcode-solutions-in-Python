from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        char1 = False
        char2 = False
        diff1 = 0
        diff2 = 0
        res = [None] * len(s)
        
        for i in range(len(s)):
            if char1: 
                res[i], diff1 = min(res[i], diff1 + 1) if res[i] else diff1 + 1, diff1 + 1
            
            if s[i] == c: 
                diff1 = 0
                res[i] = 0
                char1 = True  
            
            if char2: 
                res[len(s) - 1 - i], diff2 = min(res[len(s) - 1 - i], diff2 + 1) if res[len(s) - 1 - i] else diff2 + 1, diff2 + 1
            
            if s[len(s) - 1 - i] == c: 
                diff2 = 0
                res[len(s) - 1 - i] = 0
                char2 = True
        return res

solution = Solution()

s = "loveleetcode"
c = "e"
print(solution.shortestToChar(s,c))