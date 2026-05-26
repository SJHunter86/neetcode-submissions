class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        my_set = set(nums)

        for num in nums:
            if (num - 1) not in my_set:
                length = 1
                while (num + length) in my_set:
                    length += 1
                longest = max(length, longest)
        
        return longest