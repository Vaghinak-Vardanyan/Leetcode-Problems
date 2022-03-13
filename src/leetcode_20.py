
# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []

        for parenthes in s:
            if parenthes in "[{(":
                stack.append(parenthes)
            else:
                if not stack:
                    return False

                stack_top = stack.pop()

                if stack_top == "(" and parenthes != ")":
                    return False

                if stack_top == "{" and parenthes != "}":
                    return False

                if stack_top == "[" and parenthes != "]":
                    return False

        if stack:
            return False

        return True


print(Solution().isValid("()[]{}"))
