""" 
3. Longest Substring Without Repeating Characters
"""



class Solution:  # O(1) Time complexity and O(n) space complexity
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxx = 0
        index = [-1] * 127

        for j in range(len(s)):
            asci = ord(s[j])
            
            if index[asci] >= start:
                start = index[asci] + 1

            index[asci] = j

            lenght = j - start + 1
            if lenght > maxx:
                maxx = lenght

        return maxx
    
    
def main():
    solution = Solution()

    # Testcase
    string = "abcabcbb"
    result = solution.lengthOfLongestSubstring(string)
    print(f"Longest Substring: {result}")

if __name__ == "__main__":
    main()