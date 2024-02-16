from typing import List

class Solution:
    def marge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        result = [intervals[0]]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]

            pre = result[-1]
            # print(result[1])
            if start <= pre[1]:
                pre[1] = max(pre[1], end)
            else:
                result.append(intervals[i])

        return result
        
        
solution = Solution()

# TestCase

intervals = [[1,3],[2,6],[8,10],[15,18]]

print(solution.marge(intervals))