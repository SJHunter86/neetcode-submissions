class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1

        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        
        return nums[lo]

"""
- has to be binary search
- need to get the conditional for when to move lo and hi
- adjust pointer to throw away the larger values

- if l < m > h
[3,4,5,6,1,2]
l    
     m     
           h

[4,5,0,1,2,3]
l    
     m     
           h
"""