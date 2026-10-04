class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1

        while lo <= hi:
            mid = (lo+hi)//2 # standard mid
            if nums[mid] == target:
                return mid
                
            if nums[lo] <= nums[mid]: # left is sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1

"""
[3,4,5,6,1,2] - 1
 l
     m
           h
"""