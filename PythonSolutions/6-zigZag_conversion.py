""" 
6. Zigzag Conversion
"""

class Solution:  # O(1) Time complexity and O(1) space complexity
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        count = 0
        a = (numRows - 1) * 2
    
        if not s or not s or numRows == 1:
            return s
    
        malloc_size = [''] * (length + 1)
    
        for i in range(numRows):
            j = i
            b = 1
            while j < length:
                malloc_size[count] = s[j]
                count += 1
                if i == 0 or i == numRows - 1:
                    j += a
                elif b:
                    j += a - i * 2
                    b = 0
                else:
                    j += i * 2
                    b = 1
    
        return ''.join(malloc_size)
    
    
def main():
    s = "PAYPALISHIRING"
    numRows = 3
    solution = Solution()
    result = solution.convert(s, numRows) 
    print(result)
    
    
if __name__ == '__main__':
    main()