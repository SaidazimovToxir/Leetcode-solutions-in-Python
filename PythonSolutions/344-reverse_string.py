from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # s.reverse()
        for i in range(len(s) // 2):
            s[i], s[-i-1] = s[-i-1], s[i]
            
        return s
        
solution = Solution()

# TestCase
s = ["h","e","l","l","o"]
print(solution.reverseString(s))