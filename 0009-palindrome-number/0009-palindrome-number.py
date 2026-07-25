class Solution:
    def isPalindrome(self, x: int) -> bool:

        X = str(x)
        l = 0
        r = len(X) -1
        is_palindrome = True

        while l < r:
            if X[l] == X[r]:
                l += 1
                r -= 1
            else:
                is_palindrome = False
                return is_palindrome

        if is_palindrome:
            return True