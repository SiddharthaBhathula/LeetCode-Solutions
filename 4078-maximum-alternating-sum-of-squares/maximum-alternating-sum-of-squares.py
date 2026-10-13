class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [abs(num) for num in nums]
        nums.sort(reverse = True)
        even = sum(num**2 for num in nums[:ceil(n/2)])
        odd = sum(num**2 for num in nums[ceil(n/2):])
        return even - odd
        