from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        hashMap = {}
        
        for i in arr:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
                
        sort_hash = sorted(hashMap.values())
        
        for i, v in enumerate(sort_hash):
            k -= v
            if k < 0:
                return len(hashMap) - i

    
solution = Solution()

# TestCase

arr = [5,5,4]; k = 1

print(solution.findLeastNumOfUniqueInts(arr,k))
