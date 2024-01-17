""" 
7. Reverse Integer
"""


class Solution: # O(n^2) Time complexity and O(n+n) space complexity
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = -1 if x < 0 else 1
        reversed_str = str(abs(x))[::-1]
        reversed_num = int(reversed_str) * sign

        if reversed_num > INT_MAX or reversed_num < INT_MIN:
            return 0

        return reversed_num
    
def main():
    solution = Solution()
    
    x = -123
    result = solution.reverse(x)
    print(result)
    
if __name__ == '__main__':
    main()
    