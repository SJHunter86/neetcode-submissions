class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matches = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in matches:
                return [matches[diff], i]
            matches[num] = i
        return [-1, -1]