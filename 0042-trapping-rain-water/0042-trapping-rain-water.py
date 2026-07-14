class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [1]*n
        rightMax = [1]*n

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])
        
        rightMax[-1] = height[-1]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])

        water_stored = 0
        for i in range(n):
            water_stored += min(leftMax[i], rightMax[i])- height[i]

        return water_stored 
