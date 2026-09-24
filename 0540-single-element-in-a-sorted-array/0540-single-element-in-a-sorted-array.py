class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + ((r - l) // 2)
            if nums[mid] == nums[mid+1]:
                if (r - mid) % 2 == 0:
                    l = mid + 2
                else:
                    r = mid - 1
            elif nums[mid] != nums[mid+1]:
                if (r - mid) % 2 == 0:
                    r = mid
                else:
                    l = mid + 1

        return nums[r]