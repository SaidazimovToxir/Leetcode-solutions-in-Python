""" 
5. Longest Palindromic Substring
"""


def isPalindrome(s,start,end): # O(n) Time complexity and O(n) Space complexity
    while start<end:
        if s[start] != s[end]:
            return False
        start +=1
        end -=1

    return True

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        m = 1
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if isPalindrome(s,i,j) and j-i+1 > m:
                    start = i
                    m = j-i+1
        
        return s[start:start + m]
      
      
def main():
    solution = Solution()
    
    s = "babad"
    result = solution.longestPalindrome(s)
    print(result)

if __name__=='__main__':
    main()    