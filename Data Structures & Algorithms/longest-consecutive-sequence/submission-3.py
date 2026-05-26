class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in uniques:
                current = 1
                while num + current in uniques:
                    current += 1
                longest = max(longest, current)
        return longest