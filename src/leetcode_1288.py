
# 1288. Remove Covered Intervals

from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        result: int = len(intervals)
        longest: int = 0

        intervals = sorted(intervals, key=lambda interval: (interval[0], -interval[1]))

        for start, end in intervals:
            if end <= longest:
                result -= 1
            else:
                longest = end

        return result


print(Solution().removeCoveredIntervals(intervals = [[1,4],[3,6],[2,8]]))