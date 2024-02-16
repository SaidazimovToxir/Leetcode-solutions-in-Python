class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = ''.join(i if i.isdigit() else " " for i in word)
        # print(word)
                
        nums = word.split()
        # print(nums)
        
        
        unique = set()
        
        for num in nums:
            # print(int(num))
            unique.add(int(num))
            # print(unique)
            
        return len(unique)
        
        
solution = Solution()

# TestCase
word = "a123bc34d8ef34"

print(solution.numDifferentIntegers(word))