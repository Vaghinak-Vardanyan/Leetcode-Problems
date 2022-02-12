
# 2138. Divide a String Into Groups of Size k

from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        index: int = 0
        length: int = len(s)
        result: List[str] = []
        while index + k <= length:
            result.append(s[index:index + k])
            index = index + k

        if index != length:
            result.append(f"{s[index:]}{fill * (k - (length - index))}")

        return result


s = "abcdefghij" 
k = 3
fill = "x"
print(Solution().divideString(s, k, fill))