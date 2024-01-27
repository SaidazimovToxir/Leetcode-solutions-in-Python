""" 
629. K Inverse Pairs Array

Difficulty:  Hard
"""

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        modul = 10 ** 9 + 7
        a = [[0] * (k+1) for _ in range(n+1)]
        a[0][0] = 1
        
        for i in range(1, n+1):
            a[i][0] = 1
            for j in range(1, k+1):
                a[i][j] = (a[i][j-1] + a[i-1][j]) % modul
                if j >= i:
                    a[i][j] = (a[i][j]-a[i-1][j-i] + modul) % modul
        
        return a[n][k]
    
def main():
    solution = Solution()
    
    n = 3
    k = 3
    result = solution.kInversePairs(n,k)
    print(result)
    
if __name__ == '__main__':
    main()