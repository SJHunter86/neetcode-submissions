class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # how does a prefix help here
        prod = 1
        ltr = []
        for num in nums:
            ltr.append(prod)
            prod *= num

        prod = 1
        rtl = [0] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            rtl[i] = prod
            prod *= nums[i]

        result = []
        for i in range(len(nums)):
            result.append(ltr[i]*rtl[i])
        return result

"""
[1, 2, 4, 6] -> [48, 24, 12, 8]

[1, 1, 2, 8]
[48, 24, 6, 1]
"""