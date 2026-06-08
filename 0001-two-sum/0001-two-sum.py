class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0
        while i < len(nums): 
            value = target - nums[i]
            if value in seen:
                return [seen[value], i]
                break
            seen[nums[i]] = i
            i += 1

            