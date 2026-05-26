class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # make a set of the numbers
        # state variable to keep track of the longest
        # iterate - current state variable to compare
        # check set if 1 less is in the set - means its the start of a sequence
        # ascend current state when +1 is found in set, max compare at the end
        longest = 0
        uniques = set(nums)
        for num in nums:
            if num - 1 not in uniques:
                current = 1
                while num + current in uniques:
                    current += 1
                longest = max(longest, current)
        return longest