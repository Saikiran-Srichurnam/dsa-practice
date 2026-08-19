class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        multiply = 1
        newA = a
        while len(newA) * multiply < len(b):
            multiply += 1

        newA *= multiply

        if b in newA:
            return multiply
        
        newA += a
        multiply += 1
        if b in newA:
            return multiply
        
        return -1