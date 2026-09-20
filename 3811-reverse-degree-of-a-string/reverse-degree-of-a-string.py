class Solution:
    def reverseDegree(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            res += (26 - (ord(s[i])- ord('a'))) * (i + 1)

        return res
        