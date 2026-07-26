class Solution:
    def reverse(self, x: int) -> int:
        a = str(x)
        b = ""

        if x < 0:
            b = "-"
            for i in range(len(a)-1, 0, -1):
                b += a[i]
        else:
            for i in range(len(a)-1, -1, -1):
                b += a[i]

        ans = int(b)
        if ans < -2147483648 or ans > 2147483647:
            return 0

        return ans