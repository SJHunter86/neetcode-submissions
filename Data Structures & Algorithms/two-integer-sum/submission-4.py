class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matches = dict()
        for i, num in enumerate(nums):
            match = target - num
            if match in matches:
                return [matches[match], i]
            matches[num] = i
        
        return [0, 0]