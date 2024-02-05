import collections

class Solution:
    def n(self, s: str) -> int:
        dic = collections.defaultdict(int)
        
        for c in s:
            dic[c] += 1
        for i, c in enumerate(s):
            if dic[c] == 1: return i
        return -1
    
solution = Solution()

# TestCase
s = "loveleetcode"
print(solution.n(s)) # Expected