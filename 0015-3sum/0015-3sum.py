class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            n1 = nums[i]
            target = -n1

            # skip duplicate n1
            if i > 0 and nums[i] == nums[i -1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                twoSum = nums[left] + nums[right]
                if target == twoSum:
                    res.append([n1, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left/right values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            
                elif target < twoSum:
                    right -= 1
                else:
                    left += 1

        return res      
            
        