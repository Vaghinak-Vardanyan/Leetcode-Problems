
# 39. Combination Sum

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result: List[List[int]] = []

        if target == 0:
            return []

        def internal(candidates: List[int], current_comb: List[int] = [], current_sum: int = 0):
            
            if current_sum >= target:
                if current_sum == target:
                    result.append(current_comb.copy())
                return

            for i in range(len(candidates)):
                internal(candidates[i:], current_comb + [candidates[i]], current_sum + candidates[i])
        
        internal(candidates)
        return result


print(Solution().combinationSum(candidates = [2,3,5], target = 8))