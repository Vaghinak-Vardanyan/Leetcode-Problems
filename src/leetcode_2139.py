
# 2139. Minimum Moves to Reach Target Score

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        result: int = 0

        while maxDoubles > 0 and target != 1:
            if target % 2 == 1:
                target -= 1
            else:
                target //= 2
                maxDoubles -= 1

            result += 1

        if target != 1:
            result += target - 1
        
        return result


print(Solution().minMoves(3, 1))
