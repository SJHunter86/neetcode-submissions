class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        matches = defaultdict(int)
        for i, num in enumerate(nums):
            match = target - nums[i]
            if match in matches:
                return [matches[match], i]
            matches[nums[i]] = i
        
        return []