class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)
        self.res = []
        @cache
        def dp(i, curr, d):
            if d < 0: return
            if i == n :
                if d == 0 : self.res.append(curr)
                return
            if s[i] not in '()': dp(i + 1, curr + s[i], d)
            else :
                dp(i + 1, curr + s[i], d + (1 if s[i] == '(' else -1))
                dp(i +1, curr, d)
        dp(0, '', 0)
        ml = max(len(st) for st in self.res)
        out = [st for st in self.res if len(st) == ml]
        return out
        