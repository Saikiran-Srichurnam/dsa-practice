class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        currentArea = 0

        left = 0
        right = len(height) - 1
        while left < right:
            minimum_val = min(height[left], height[right])
            currentArea = minimum_val * (right-left)
            maxArea = max(maxArea, currentArea)
            if height[left] < height[right]:
                left += 1
            # elif height[left] >= height[right]:
            else:
                right -= 1

        return maxArea