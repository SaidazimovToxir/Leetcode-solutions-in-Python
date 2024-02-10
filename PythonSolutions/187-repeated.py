class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        dic = {}
        a = " " + s[:9]
        for i in range(9, len(s)):
            a = a[1:] + s[i]
            dic[a] = 1 if a not in dic else dic[a] + 1
        return [k for k, v in dic.items() if v > 1]
    
    
solution = Solution()

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(solution.findRepeatedDnaSequences(s))