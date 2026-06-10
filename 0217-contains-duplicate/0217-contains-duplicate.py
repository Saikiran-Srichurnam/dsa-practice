class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_list = {}
        for i in range(len(nums)):
            if nums[i] in my_list:
                my_list[nums[i]] += 1
            else:
                my_list[nums[i]] = 1
    
            if my_list[nums[i]] > 1:
                return True
        return False