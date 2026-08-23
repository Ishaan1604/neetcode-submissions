class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            remainder = nums[i+1:]
            if (target - num) in remainder:
                return [i, remainder.index(target - num) + i + 1]

