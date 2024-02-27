from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
            ## METHOD ONE | Time complexity: O(n^2 log n)
        """ 
        sums = [0] 
        s = 0
        result = 0
        
        for i in nums:
            s += i
            result += len([i for i in nums if s - i >= lower and s - i <= upper])
            sums.append(s)
            sums.sort()
            
        return result 
        """
        
            ## marge sort + prefix-sum || Time complexity: O(n log n)
        c = [0]
        for num in nums:
            c.append(c[-1] + num)
            
        def margeSort(left, right):
            if left == right: return 0
            
            mid = (left + right) // 2
            
            count = margeSort(left, mid) + margeSort(mid + 1, right)
            
            i = j = mid + 1
            
            for l in c[left:mid + 1]:
                
                while i <= right and c[i] - l < lower:
                    i += 1
                    
                while j <= right and c[j] - l <= upper:
                    j += 1
                count += j - i
                
            
            print(sorted(c[left:right + 1]))
            c[left:right + 1] = sorted(c[left:right + 1])
            return count
            
        return margeSort(0, len(c) - 1)
        
        
solution = Solution()

# TestCase
# nums = [0]; lower = 0; upper = 0
nums = [-2,5,-1]; lower = -2; upper = 2



print(solution.countRangeSum(nums,lower,upper))