class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        if s == " ":
            return True
        else:
            for ch in s:
                if ch.isalnum():
                    x += ch.lower()  

            is_palindrome = True

            i = 0
            j = len(x)-1
            while i < j:
                if x[i] != x[j]:
                    is_palindrome = False
                    return is_palindrome
                i += 1
                j -= 1
            
            return is_palindrome
                    