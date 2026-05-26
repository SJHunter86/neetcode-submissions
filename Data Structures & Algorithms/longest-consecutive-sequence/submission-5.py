class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        longest = 0

        for num in uniques:
            if num - 1 not in uniques: # confirms its the beginning of a sequence
                curr = num
                count = 1
                while curr + 1 in uniques:
                    count += 1
                    curr += 1
                longest = max(longest, count)

        return longest