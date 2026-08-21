class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # Binary search for the first position where nums[i] >= target
        while l <= r:
            m = (l + r) // 2

            if nums[m] < target:
                # Target must be to the right of mid
                l = m + 1
            else:
                # nums[m] >= target, so mid could be the answer
                r = m - 1

        # l is the first index where target can be inserted
        return l

        # Time: O(log n)
        # Space: O(1)
        