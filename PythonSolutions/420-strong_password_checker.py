class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = 3
        if any('a' <= c <= 'z' for c in password): n -= 1
        if any('A' <= c <= 'Z' for c in password): n -= 1
        if any(c.isdigit() for c in password): n -= 1
        
        # print(n)

        c = 0
        a = 0
        b = 0
        i = 2
        while i < len(password):
            
            if password[i] == password[i-1] == password[i-2]:
                lenn = 2
                
                while i < len(password) and password[i] == password[i-1]:
                    lenn += 1
                    i += 1
                    
                c += lenn // 3
                
                if lenn % 3 == 0: a += 1
                elif lenn % 3 == 1: b += 1
                
            else:
                i += 1
        
        if len(password) < 6:
            # print(max(n, 6 - len(password)))
            return max(n, 6 - len(password))
        
        elif len(password) <= 20:
            return max(n, c)
        
        else:
            d = len(password) - 20
            
            c -= min(d, a)
            c -= min(max(d - a, 0), b * 2) // 2
            # print(min(max(d - a, 0), b * 2) // 2)
            c -= max(d - a - 2 * b, 0) // 3
                
            return d + max(n, c)

solution = Solution()

# TestCase

p = "aA1"

print(solution.strongPasswordChecker(p))




    # prefix-sum + merge-sort | time complexity: O(nlogn)
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        cumsum = [0]
        for n in nums:
            cumsum.append(cumsum[-1]+n)
            
		# inclusive
        def mergesort(l,r):
            if l == r:
                return 0
            mid = (l+r)//2
            cnt = mergesort(l,mid) + mergesort(mid+1,r)
			
            i = j = mid+1
            # O(n)
            for left in cumsum[l:mid+1]:
                while i <= r and cumsum[i] - left < lower:
                    i+=1
                while j <= r and cumsum[j] - left <= upper:
                    j+=1
                cnt += j-i
                
            cumsum[l:r+1] = sorted(cumsum[l:r+1])
            return cnt
			
        return mergesort(0,len(cumsum)-1)