
# # 171. Excel Sheet Column Number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result: int = 0

        for letter in columnTitle:
            result *= 26 
            result += ord(letter) - ord('A') + 1

        return result


print(Solution().titleToNumber("ZY"))