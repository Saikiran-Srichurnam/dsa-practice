class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxWater = 0
        currArea = 0
        i = 0
        j = len(height) - 1
        while i < j:
            minVal = min(height[i], height[j])
            currArea = minVal * (j - i)
            maxWater = max(currArea, maxWater)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
        return maxWater