class Solution:
    def reverseStr(slef, s: str, k: int) -> str:
        # return "".join([s[i:i+k][::-1]+s[i+k:i+2*k]   if len(s)>=i or len(s)>i-k else s[k*i:][::-1] for i in range(0,len(s),k*2)])
        n = "".join([s[i:i+k][::-1]+s[i+k:i+2*k] for i in range(0, len(s), k*2)])
        print(n)
        
        
        
solution = Solution()

# TestCase
s = "abcdefg"; k = 2

print(solution.reverseStr(s,k))