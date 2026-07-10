class Solution(object):
    def isValid(self, s):
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:

            # If opening bracket, push onto stack
            if ch in "({[":
                stack.append(ch)

            # Otherwise, it's a closing bracket
            else:
                # No opening bracket available
                if not stack:
                    return False

                # Top of stack doesn't match
                if stack[-1] != pairs[ch]:
                    return False

                # Matched, remove opening bracket
                stack.pop()

        # Valid only if nothing is left unmatched
        return len(stack) == 0