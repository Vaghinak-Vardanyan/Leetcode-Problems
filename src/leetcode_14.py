
# 14. Longest Common Prefix

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result: str = ""

        first: str = strs[0]
        for index, char in enumerate(first):
            not_prefix: bool = False
            for word in strs[1:]:
                if index >= len(word) or word[index] != char:
                    not_prefix = True
                    break
            
            if not_prefix:
                break
            result += char

        return result

print(Solution().longestCommonPrefix(["flower","flow","flight"]))