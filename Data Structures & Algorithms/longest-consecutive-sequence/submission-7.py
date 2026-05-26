class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set of ints from nums
        unique = set(nums)
        # track longest
        longest = 0

        # iterate the list of nums
        for num in nums:
            if num - 1 not in unique:
                seq = 1
                curr = num
                while curr + 1 in unique:
                    seq += 1
                    curr += 1
                longest = max(longest, seq)
        
        return longest
