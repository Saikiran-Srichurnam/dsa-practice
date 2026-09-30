class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        i = 0
        j = len(nums)
        while i < j:
            value = target - nums[i]
            if value not in seen:
                seen[nums[i]] = i
            else:
                return [seen[value], i] 
            
            i += 1