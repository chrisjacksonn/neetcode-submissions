class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):

            # case 1
            if i == len(word):
                return True

            # case 2:
            if (min(r, c) < 0 or # either (min) coordinate is negative
                r >= ROWS or c >= COLS or # off the grid (positive)
                word[i] != board[r][c] or # current cell doesn't match letter
                (r, c) in path): # repeat cell
                return False

            path.add((r, c)) # mark cell as used for this attempt
            # check right, left, up, and below current cell
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c)) # free cell up for backtracking
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): # try the word search from every cell
                    return True
        return False