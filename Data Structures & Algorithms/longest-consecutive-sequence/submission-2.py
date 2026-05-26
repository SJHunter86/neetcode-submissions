class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # track longest sequence and current sequence
        # need a set of the nums in the list
        # only compute if there is no number that is 1 less than current number (start of sequence)
        # while loop to count if there are numbers + current length
        if len(nums) == 0:
            return 0
        longest = 1
        unique = set(nums)
        for num in nums:
            if num - 1 not in unique:
                current = 1
                while num + current in unique:
                    current += 1
                longest = max(longest, current)
        return longest