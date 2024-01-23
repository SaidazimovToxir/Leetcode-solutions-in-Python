class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        result, stack = 0, []
        arr.copy()
        arr.insert(0, float('-inf'))
        arr.append(float('-inf'))
        
        for i,j in enumerate(arr):
            while stack and arr[stack[-1]] > j:
                curr = stack.pop()
                result += arr[curr] * (i-curr) * (curr-stack[-1])
            stack.append(i)
        return result % (10 ** 9 + 7)
        
        
def main():
    solution = Solution()
    
    test = [3,1,2,4]
    result = solution.sumSubarrayMins(test)
    print(result)
    
if __name__ == '__main__':
    main()