class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        first = False

        for i in range(n):
            if nums[i] == i:
                continue

            if not first:
                res = nums[i]
                first = True
            else:
                res &= nums[i]

        return res