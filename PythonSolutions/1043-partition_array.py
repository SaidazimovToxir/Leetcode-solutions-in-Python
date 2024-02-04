""" 
1043. Partition Array for Maximum Sum

Difficulty: Medium
"""



from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        a = [0] * (n + 1)
        
        for i in range(1, n+1):
            curr_m = 0
            for j in range(1, min(i, k)+1):
                curr_m = max(curr_m, arr[i-j])
                a[i] = max(a[i], a[i-j] + curr_m * j)
                
        return a[n]
    
def main():
    solution  = Solution()
    
    # Testcase
    arr = [1,15,7,9,2,5,10] 
    k = 3 # Expect 84.
    
    result = solution.maxSumAfterPartitioning(arr, k)
    print(result)
    
if __name__ == "__main__":
    main()
