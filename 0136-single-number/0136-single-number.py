class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # using xor operation to solve single number
        xor = 0
        for i in range(len(nums)):
            xor = xor ^ nums[i]
        return xor