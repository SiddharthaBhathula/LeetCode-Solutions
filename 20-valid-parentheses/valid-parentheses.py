class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines whether the given string contains valid parentheses.

        A string is valid when:
        1. Every opening bracket has a matching closing bracket.
        2. Brackets are closed in the correct order.
        3. The bracket types match: (), {}, [].

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        # Stack stores the opening brackets we encounter.
        stack = []

        # Map each closing bracket to its corresponding opening bracket.
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:

            # If it is an opening bracket, push it onto the stack.
            if char in "({[":
                stack.append(char)

            else:
                # A closing bracket cannot appear if there is
                # no corresponding opening bracket in the stack.
                if not stack:
                    return False

                # The latest opening bracket must match
                # the current closing bracket.
                if stack.pop() != bracket_map[char]:
                    return False

        # The stack must be empty after processing the entire string.
        # If brackets remain, some opening brackets were never closed.
        return len(stack) == 0
        