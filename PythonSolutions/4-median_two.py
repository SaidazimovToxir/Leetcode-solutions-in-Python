""" 
4. Median of Two Sorted Arrays
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1+=nums2
        nums1.sort()

        lenght=len(nums1)
        if lenght%2==0:
            a = lenght//2
            return (nums1[a-1] + nums1[a]) / 2.0
        else:
            a = lenght//2
            return float(nums1[a])
        
def main():
    solution = Solution()
    
    # Testcase
    nums1 = [1,3] 
    nums2 = [2]
    result = solution.findMedianSortedArrays(nums1,nums2)
    print(result)
    print("Hello world")
    
if __name__=='__main__':
    main()