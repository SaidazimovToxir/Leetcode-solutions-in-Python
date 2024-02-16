from typing import List
from collections import Counter

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # def check(s, i):
        #     for c in s:
        #         i = s.find(c, i) + 1
        #         if not i: return False
        #     return True
        # return sum((check(word, 0) for word in words))
        # lst=list(words)
        # s=Counter(s)
        # for i in words:
        #     word=i
        #     i=Counter(i)
        #     for j in i.keys():
        #         if j not in s or i[j]!=s[j]:
        #             words.remove(word)
        #             print(word)
        # return len(words)
        def check(words):
            i = -1
            for c in words:
                i = s.find(c, i + 1)
                if i == -1: return False
            return True
        return sum(map(check, words))
        # lst=list(words)
        # s=Counter(s)
        # for i in words:
        #     word=i
        #     i=Counter(i)
        #     for key in i.keys():
        #         if key not in s or i[key]>s[key]:
        #             lst.remove(word)
        #             print(lst)
        #             break
        # return len(lst)

    
    
solution = Solution()

# TestCase
s = "abcde"; words = ['dac']
# s = "dsahjpjauf"; words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]

print(solution.numMatchingSubseq(s,words))