# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        res = 0
        while l <= r:
            mid = l + ((r -l)//2)
            ans = isBadVersion(mid)
            if ans:
                res = mid 
                r = mid - 1
            else:
                l = mid + 1

        return res
