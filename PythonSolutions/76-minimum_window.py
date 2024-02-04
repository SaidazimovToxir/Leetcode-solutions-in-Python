""" 
76. Minimum Window Substring

Difficulty: Hard
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_s = {}
        cnt_t = {}
        n = len(s)
        left = set(t)
        r = -1
        
        
        for c in t:
            cnt_t[c] = cnt_t.get(c, 0) + 1
        L = l = 0
        while left:
            r += 1
            if r >= n:
                return ""
            cnt_s[s[r]] = cnt_s.get(s[r], 0) + 1
            if s[r] in cnt_t and cnt_s[s[r]] == cnt_t[s[r]]:
                left.discard(s[r])
        R = r
        cnt_s[s[r]] -= 1
        while l < r < n:
            cnt_s[s[r]] = cnt_s.get(s[r], 0) + 1
            while s[l] not in cnt_t or cnt_s[s[l]] > cnt_t[s[l]]:
                cnt_s[s[l]] -= 1
                l += 1
            if r - l < R - L:
                L, R = l, r
            r += 1   
        return s[L: R + 1]
    
    
def main():
    solution = Solution()
    
    # TestCase
    s = "ADOBECODEBANC"
    t = "ABC"
    
    result = solution.minWindow(s,t)
    print(result) # expect "BANC"

if __name__ == "__main__":
    main()