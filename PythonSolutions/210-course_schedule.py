from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        children, parent = defaultdict(set), defaultdict(set)
        for i, j in prerequisites: children[i].add(j); parent[j].add(i)
        stack = [i for i in range(numCourses) if not children[i]]
        for i in stack:
            for j in parent[i]:
                children[j].remove(i)
                if not children[j]: stack += j,
        return stack if len(stack) == numCourses else []
    
    
    
solution = Solution()

# TestCase
numCourses = 2; prerequisites = [[1,0]]

print(solution.findOrder(numCourses,prerequisites))