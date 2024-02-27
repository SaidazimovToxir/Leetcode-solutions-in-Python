class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1  == "" or word2 == "":
            return len(word2) or len(word1)
        lst = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        # print(lst)
        

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):

                if not (i or j):
                    lst[i][j] = i or j

                elif word1[i - 1] == word2[j - 1]:
                    lst[i][j] += lst[i - 1][j - 1]

                else:
                    lst[i][j] += min(lst[i - 1][j], lst[i][j - 1], lst[i - 1][j - 1]) + 1
                    
        print(lst)

        return lst[len(word1)][len(word2)]
        
        
solution = Solution()

# TestCase

word1 = "sea"; word2 = "ate"
# word1 = "intention"; word2 = "execution"
# word1 = "horse"; word2 = "ros"

print(solution.minDistance(word1, word2))




""" 
arr1[0]=1:
1 + 4 > 3
1 + 3 > 3
1 - 6 > 3
1 - 10 > 3
1 - 20 > 3
1 - 30 > 3

arr1[1] = 4
8 > 3
7 > 3
2 < 3
6 > 3
14 > 3
26 > 3

arr1[2] = 2
6 > 3
5 > 3
4 > 3
8 > 3
18 > 3
28 > 3

arr1[3] = 3
7 > 3 
6 > 3
3 <= 3
7 > 3
17 > 3
27 > 3
"""