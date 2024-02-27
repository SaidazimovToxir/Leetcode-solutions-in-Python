from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        index = {v:i for i,v in enumerate(words)}
        result = []
        
        for i, v in enumerate(words):
            for j in range(len(v) + 1):
                
                p = v[:j]
                s = v[j:]

                if p == p[::-1]:
                    s = s[::-1]
                    
                    if s != v and s in index:
                        # print([index[s], i])
                        result.append([index[s], i])
                        
                if j != len(v) and s == s[::-1]:
                    p = p[::-1]
                    
                    if p != v and p in index:
                        # print([i, index[p]])
                        result.append([i, index[p]])
                        
        return result
        
solution = Solution()

# TestCase
# words = ["abcd","dcba","lls","s","sssll"]
words = ["a",""]

print(solution.palindromePairs(words))
