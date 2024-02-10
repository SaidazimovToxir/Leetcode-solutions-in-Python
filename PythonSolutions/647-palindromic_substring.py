class Solution:
    def countSubstrings(self, s: str) ->  int:       
        res = 0
        for k in range(len(s)):
            i = j = k
            
            while 0 <= i and j < len(s):
                if s[i] == s[j]: 
                    res += 1
                else: 
                    break
                i = i - 1
                j = j + 1
            i = k
            j = k + 1
            
            while 0 <= i and j < len(s):
                if s[i] == s[j]: 
                    res += 1
                else: 
                    break
                i = i - 1
                j = j + 1
        return res
    
    
solution = Solution()

# TestCase
s = "abc"
print(solution.countSubstrings(s))
