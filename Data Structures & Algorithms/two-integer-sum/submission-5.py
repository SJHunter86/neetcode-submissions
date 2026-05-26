class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matches = {}

        for i, num in enumerate(nums):
            curr = target - nums[i]
            if curr in matches:
                return [matches[curr], i]
            matches[nums[i]] = i
        
        return [0, 0]