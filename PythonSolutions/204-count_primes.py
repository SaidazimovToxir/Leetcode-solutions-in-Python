class Solution:
    def countPrimes(self,n):
        if n <= 2:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if isPrime[i]:
                # print(i)
                for j in range(i*i, n, i):
                    # print(j)
                    isPrime[j] = False

        # print(isPrime)
        count = sum(isPrime)
        return count
    
    
def main():
    solution = Solution()
    
    n = 100
    result = solution.countPrimes(n)
    print(result)

if __name__ == '__main__':
    main()

# print(int(10**0.5))