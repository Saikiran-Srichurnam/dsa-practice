class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []

        # Sort the array to use the two-pointer approach
        nums.sort()
        result = []

        # Fix one element and find the other two using two pointers
        for i in range(len(nums)-2):

            # Skip duplicate first elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -(nums[i])
            left, right = i + 1, len(nums) - 1

            while left < right :
                if nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left  += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
            
        return result
            

        
