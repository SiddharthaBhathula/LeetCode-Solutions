class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp = {}
        for k, v in knowledge: mp[k] = v
        res = []
        curr = []
        started = False

        for c in s:
            if c == '(':
                started = True
            elif c == ')':
                    started = False
                    join = "".join(curr)
                    res.append(mp[join] if join in mp else '?')
                    curr = []
            else:
                    if started: curr.append(c)
                    else: res.append(c)
        return "".join(res)        