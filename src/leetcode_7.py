
# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        int_max = 2147483647
        int_min = -2147483648
        sign_multiplier = 1 
        result: int = 0

        if x < 0:
            sign_multiplier = -1
            x = -x

        while x:
            last_digit = x % 10
            x //= 10
            result = result * 10 + last_digit
            

        if sign_multiplier * result > int_max or sign_multiplier * result < int_min:
            return 0


        return result


print(Solution().reverse(-255))
print(Solution().reverse(3258721))