
# 402. Remove K Digits

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if len(num) <= k:
            return "0"

        stack: list[str] = []

        for digit in num:
            while stack and k and stack[-1] > digit:
                stack.pop()
                k -= 1

            if stack or digit != "0":
                stack.append(digit)

        if k:
            stack = stack[0: -k]

        return "".join(stack) or "0"


print(Solution().removeKdigits(num = "112", k = 1))