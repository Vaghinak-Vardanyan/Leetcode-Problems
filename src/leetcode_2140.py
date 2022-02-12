# 2140. Solving Questions With Brainpower

from typing import List

class Solution:
    
    def mostPoints(self, questions: List[List[int]]) -> int:
        length: int = len(questions)
        results: List[int] = [0] * length

        results[length - 1] = questions[length - 1][0]

        for i in range(length - 2, -1, -1):
            if i + questions[i][1] + 1 < length:
                results[i] = max(results[i + 1], questions[i][0] + results[i + questions[i][1] + 1])
            else:
                results[i] = max(results[i + 1], questions[i][0])

        return results[0]
    
questions = [[3,2],[4,3],[4,4],[2,5]]
print(Solution().mostPoints(questions))