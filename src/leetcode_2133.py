from typing import Iterable, List

# 2133. Check if Every Row and Column Contains All Numbers

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for i in range(n):
            row_sum: int = 0
            column_sum: int = 0

            for j in range(n):
                row_sum = row_sum ^ matrix[i][j] ^ (j + 1)
                column_sum = column_sum ^ matrix[j][i] ^ (j + 1)

            if (row_sum or column_sum):
                return False

        return True



print(Solution().checkValid([[1,2,3],[3,1,2],[2,3,1]]))
print(Solution().checkValid([[1]]))