
# 2136. Earliest Possible Day of Full Bloom

from typing import List

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        seeds: List[int] = sorted(range(len(plantTime)), key=lambda x: (-growTime[x], -plantTime[x]))
        max_bool_days:int = 0
        bloom_days: int = 0
        plant_days: int = 0

        for seed in seeds:
            bloom_days = plant_days + growTime[seed] + plantTime[seed]
            max_bool_days = max(bloom_days, max_bool_days)
            plant_days += plantTime[seed]

        return max_bool_days