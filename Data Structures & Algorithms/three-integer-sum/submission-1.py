class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums)-2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            lo, hi = i+1, len(nums)-1
            while lo < hi:
                curr = nums[i] + nums[lo] + nums[hi]
                if curr == 0:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                elif curr < 0:
                    lo += 1
                else:
                    hi -= 1
            i += 1
        return res