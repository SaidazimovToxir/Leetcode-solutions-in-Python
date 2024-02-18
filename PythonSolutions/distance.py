class Solution:
    def minDistance(self, word1: str, word2: set) -> int:
        lst = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]
        # print(lst)
        
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                
                # if not (i and j):
                #     lst[i][j] = i or j
                    # print(lst)
                
                if word1[i - 1] == word2[j - 1]:
                    lst[i][j] += lst[i - 1][j - 1]
        
                else:
                    lst[i][j] += min(lst[i - 1][j], lst[i][j - 1], lst[i - 1][j - 1]) + 1
                    
        return lst[-1][-1]
        
        
solution = Solution()

# TestCase

word1 = "horse"; word2 = "ros"

print(solution.minDistance(word1, word2))