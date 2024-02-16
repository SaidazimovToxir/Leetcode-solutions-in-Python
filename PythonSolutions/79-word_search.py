from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, o = len(board), len(board and board[0]), len(word)
        def explore(i, j, k, q):
            for x, y in ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)):
                if k>=o or (0<=x