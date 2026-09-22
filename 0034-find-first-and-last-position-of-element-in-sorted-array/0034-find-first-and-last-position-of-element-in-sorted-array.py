class Solution:

    def findLeftPos(self, nums:list[int], target:int, n:int ) -> int:
        leftPos = -1

        l = 0 
        r = n - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                leftPos = mid
                r = mid -1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return leftPos

    def findRightPos(self, nums:list[int], target:int, n:int ) -> int:
        rightPos = -1

        l = 0 
        r = n - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                rightPos = mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return rightPos


    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        leftPos = self.findLeftPos(nums, target, n)
        rightPos = self.findRightPos(nums, target, n)

        return [leftPos, rightPos]
                