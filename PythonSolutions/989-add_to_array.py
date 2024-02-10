from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # for i in range(len(num))[::-1]:
        #     num[i] = (num[i] + k) % 10
        #     k = (num[i] + k) // 10
        
        # return [int(i) for i in str(k)] + num if k else num
        l = 0
        r = len(num) - 1
        
        while k or l:
            if r >= 0:
                dSum = num[r] + k % 10 + l
                num[r] = dSum % 10
                l = dSum // 10
                r -= 1
            
            else:
                dSum = k % 10 + l
                num.insert(0,dSum%10)
                l = dSum // 10
                
            k //= 10
        return num


solution = Solution()
num = [2,1,5]; k = 806
print(solution.addToArrayForm(num,k))