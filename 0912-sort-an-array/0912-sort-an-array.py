class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base case
        if len(nums) <= 1:
            return nums

        # Split
        mid = len(nums) // 2

        # Sort left
        left = nums[:mid]
        
        # Sort right
        right = nums[mid:]

        left = self.sortArray(left)
        right = self.sortArray(right)

        # Merge
        return self.merge(left, right)

    # Merge logic
    def merge(self, left, right):
        ans = []

        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            elif left[i] > right[j]:
                ans.append(right[j])
                j += 1
        
        while i < len(left):
            ans.append(left[i])
            i += 1
        
        while j < len(right):
            ans.append(right[j])
            j += 1
        
        return ans
