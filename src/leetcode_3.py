
# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        
        length: int = len(s)
        result: int = 1
        
        for i in range(2, length + 1):
            window: dict[str, int] = {}
            start: int = 0
            end: int = i

            while start < end:
                if s[start] not in window:
                    window[s[start]] = start
                    start += 1
                else:
                    start = window[s[start]] + 1
                    window.clear()
                    end = start + i
                    if end > length:
                        return result
            
            result = i

        return result

print(Solution().lengthOfLongestSubstring("aab"))