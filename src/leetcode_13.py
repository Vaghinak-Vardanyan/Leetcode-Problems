
# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        int_by_roman: dict =  {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        length: int = len(s)
        result: int = 0

        for i, char in enumerate(s):
            if i + 1 < length and int_by_roman[s[i + 1]] > int_by_roman[s[i]]:
                result -= int_by_roman[s[i]]
            else:
                result += int_by_roman[s[i]]

        return result


print(Solution().romanToInt("IV"))