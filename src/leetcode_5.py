# 5. Longest Palindromic Substring

class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        result: str = ""

        for i in range(0, len(s)):
            local_result = self.expandCentre(s, i, i)
            if len(local_result) > len(result):
                result = local_result

            local_result = self.expandCentre(s, i, i + 1)
            if len(local_result) > len(result):
                result = local_result

        return result


    def expandCentre(self, s: str, left: int, right: int) -> str:
        result: str = ""
        result_length: int = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if result_length < right - left + 1:
                result = s[left:right+1]
                result_length = right - left + 1
            left -= 1
            right += 1
        
        return result


solution = Solution()

print(solution.longestPalindrome("cbbd"))
print(solution.longestPalindrome("a"))