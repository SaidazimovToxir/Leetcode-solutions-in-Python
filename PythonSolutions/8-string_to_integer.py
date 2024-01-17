""" 
8. String to Integer (atoi)
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        a, count, booln = 0, 0, 0

        if not s:
            return 0

        while s and s[0] == ' ':
            s = s[1:]

        if s and s[0] == '-':
            booln = 1
            s = s[1:]
        elif s and s[0] == '+':
            s = s[1:]

        while s and s[0].isdigit():
            a = int(s[0])

            if booln == 0:
                if count > (INT_MAX - a) // 10:
                    return INT_MAX

                count = count * 10 + a
            else:
                if count < (INT_MIN + a) // 10:
                    return INT_MIN

                count = count * 10 - a

            s = s[1:]

        return count
    
    
def main():
    solution = Solution()
    
    s = "  -42"
    result = solution.myAtoi(s)
    print(result)


if __name__ == '__main__':
    main()