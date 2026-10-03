class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        uniques = set(nums) # O(n)
        longest = 1

        for num in nums:
            if num - 1 in uniques:
                continue
            curr_longest = 1
            curr = num
            while curr+1 in uniques:
                curr_longest += 1
                curr = curr + 1
            longest = max(longest, curr_longest)
        
        return longest

"""
longest = 1
[2,20,4,10,3,4,5]
add them all to a set for instant lookup
while loop inside the check to see if num + 1 is found in the set?
"""