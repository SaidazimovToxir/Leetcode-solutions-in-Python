from typing import List

class Soluiton:
    def stoneGame(self, stones: List[int]) -> bool:
        count = [0, 0, 0]  # count[0]: remainder 0, count[1]: remainder 1, count[2]: remainder 2
        for i in stones:
            count[i % 3] += 1

        if count[0] % 2 == 0:
            return count[1] > 0 and count[2] > count[1] or count[2] > 0 and count[1]>count[2] - 1 
        else:
            return count[1] > 0 and count[2] < count[1] - 2 or count[2] > 0 and count[1] < count[2] - 2

        
        
solution = Soluiton()

# TestCase
stones = [20,3,20,17,2,12,15,17,4]

    

print(solution.stoneGame(stones))
