class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sett = set(numbers)
        for i, num in enumerate(numbers):
            if (target - num) in sett:
                return [i + 1, numbers[i+1:].index(target-num) + i + 2]