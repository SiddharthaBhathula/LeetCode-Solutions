class Solution:
    def checkString(self, s: str) -> bool:
        seenb = False

        for c in s:
            if c == 'b': seenb = True
            elif c == 'a' and seenb: return False

        return True