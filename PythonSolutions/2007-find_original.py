from typing import List
from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        result = []
        counter = Counter(changed)
        
        for num in sorted(changed, key=abs):
            if counter[num] > 0 and counter[2 * num] > 0:
                result.append(num)
                counter[num] -= 1
                counter[2 * num] -= 1

        return result if len(result) == len(changed) // 2 else []


solution = Solution()
changed = [6,3,0,1]
print(solution.findOriginalArray(changed))
