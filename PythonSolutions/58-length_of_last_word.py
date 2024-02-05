""" 
58. Length of Last Word

Difficulty: Easy
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # if s==0: return 0
        count=0
        count2=0
        for i in s:
            if count > 0:
                count2 = count
            if i == ' ':
                count=0
                continue
            count+=1
        if count > 0:
            return count
        else:
           return count2
       
       
solution = Solution()

# TestCase
s = "Hello World"
print(solution.lengthOfLastWord(s)) # Expected 5