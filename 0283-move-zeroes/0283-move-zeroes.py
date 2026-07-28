class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
            i += 1
        
        while pos < len(nums):
            nums[pos] = 0
            pos += 1
        
        return nums
        