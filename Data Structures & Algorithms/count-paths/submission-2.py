class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            # row being built will have as many cells as there are columns (n)
            newRow = [1] * n
            for j in range(n - 2, -1, -1): # (start, stop, step): start at second last element, so that final element stays as 1
                newRow[j] = newRow[j + 1] + row[j] # curr = right + below
            row = newRow
        return row[0]