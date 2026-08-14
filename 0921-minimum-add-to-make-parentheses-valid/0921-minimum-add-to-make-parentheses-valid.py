class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openBracket = 0 #number of opening brackets needed
        size = 0

        for ch in s:
            if ch == "(":
                size +=1
            elif ch ==")" and size > 0:
                size -= 1
            elif ch == ")" and size == 0:
                openBracket += 1
        
        return size + openBracket