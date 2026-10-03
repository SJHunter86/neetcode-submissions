class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matches = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in matches:
                return [matches[comp], i]
            matches[num] = i