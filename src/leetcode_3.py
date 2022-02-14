
# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        result: int = 0
        window: list[int | None] = [None] * 128
        left: int = 0
        right: int = 0

        while right < len(s):

            current = s[right]

            index = window[ord(current)]
            if index != None and left <= index < right:
                left = index + 1

            result = max(result, right - left + 1)

            window[ord(current)] = right
            right += 1

        return result

print(Solution().lengthOfLongestSubstring("au"))