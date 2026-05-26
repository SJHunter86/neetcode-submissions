class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        longest = 0

        for num in uniques:
            if num - 1 not in uniques: # start of a sequence
                count = 1
                while num + count in uniques:
                    count += 1
                longest = max(longest, count)
        
        return longest