class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        my_list = {}
        for i in range(n+1):
            if i not in my_list:
                my_list[i] = 0
            
            if i in nums:
                my_list[i] = 1
            
            if my_list[i] != 1:
                ans = i
            
        return ans