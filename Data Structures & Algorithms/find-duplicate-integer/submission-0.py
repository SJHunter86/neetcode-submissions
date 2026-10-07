class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        flag = 0
        while flag != slow:
            slow = nums[slow]
            flag = nums[flag]
        
        return flag