class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            print(True)
        else:
            newStr = ""
            for ch in s:
                if ch.isalnum():
                    newStr += ch.lower()
                    
            left = 0
            right = len(newStr) - 1
            isPalindrome = True

            while left < right:
                if newStr[left] != newStr[right]:
                    isPalindrome = False
                    return isPalindrome
                left += 1
                right -= 1
                
            if isPalindrome:
               return isPalindrome
            else:
                return isPalindrome
                        
                    