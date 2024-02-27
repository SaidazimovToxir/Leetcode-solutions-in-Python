class Solution:
    def nearestPalindromic(self, n: str) -> str:
        k = len(n)
        lst = [str(10**i + j) for i in (k - 1, k) for j in (-1, 1)]
        print(lst)
        
        h = n[:(k+1)//2]
        
        p = int(h)
        
        for i in map(str, (p - 1, p, p + 1)):
            lst.append(i + (i[:-1] if k % 2 else i)[::-1])
        
        # print(lst)
            
        def func(x):
            return abs(int(n) - int(x))
        
        result = None
        for m in lst:
            if m != n and not m.startswith('00'):
                if (result is None or func(m) < func(result) or func(m) == func(result) and int(m) < int(result)):
                    result = m
                    
                    
        return result
                    
solution = Solution()

# TestCase

n = "807045053224792883" # 807045053350540708

print(solution.nearestPalindromic(n))