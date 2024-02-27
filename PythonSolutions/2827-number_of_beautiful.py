class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def beautiful(num):
            n = str(num)
            even = sum(1 for digit in n if int(digit) % 2 == 0)
            odd = len(n) - even
            return even == odd and num % k == 0
        
        count = 0
        
        for i in range(low, high + 1):
            if beautiful(i):
                count += 1
        
        return count
    
soluiton = Solution()

# TestCase
low = 349863935; high = 772153463; k = 11

print(soluiton.numberOfBeautifulIntegers(low,high,k))