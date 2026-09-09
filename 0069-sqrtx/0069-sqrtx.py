class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left = 0
        right = x
        answer = 0
        while left <= right:
            mid = left + ((right - left) // 2)
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
                answer = mid
            else:
                return mid
        
        return answer
            