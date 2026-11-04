class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        l = SortedList()
        h = SortedList()
        ls, hs = 0, 0
        vals = [0] * n

        for i in range(n):
            if not h or nums[i] >= h[0][0]:
                h.add([nums[i], i])
                hs += nums[i]
            else:
                l.add([nums[i], i])
                ls += nums[i]

            if i >= x:
                val = nums[i - x]
                if [val, i - x] in l:
                    l.discard([val, i - x])
                    ls -= val
                else:
                    h.discard([val, i - x])
                    hs -= val

            while len(h) > len(l) + 1:
                val, idx = h.pop(0)
                hs -= val
                l.add([val, idx])
                ls += val

            while len(h) < len(l):
                val, idx = l.pop(-1)
                ls -= val
                h.add([val, idx])
                hs += val

            if i >= x - 1:
                vals[i] = ((len(l) * h[0][0]) - ls) + (hs - (len(h) * h[0][0]))

        dp = [[float('inf')] * (k + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 0

        dp[x - 1][1] = vals[x - 1]

        for i in range(x, n):
            for j in range(1, k + 1):
                dp[i][j] = min(dp[i - 1][j], vals[i] + dp[i - x][j - 1])

        return dp[n - 1][k]
        