class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        # Compare characters from both ends
        while l < r:

            # Skip non-alphanumeric characters
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            # Compare characters ignoring case
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


# Time: O(n)
# Space: O(1)