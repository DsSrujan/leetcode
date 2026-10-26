
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1
        i = 0

        while i < len(s):
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '+':
                result += sign * num
                num = 0
                sign = 1

            elif ch == '-':
                result += sign * num
                num = 0
                sign = -1

            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1

            elif ch == ')':
                result += sign * num
                num = 0

                result *= stack.pop()
                result += stack.pop()

            i += 1

        result += sign * num
        return result
