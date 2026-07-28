class Solution:
    def secondHighest(self, s: str) -> int:

        larNum = -1
        secondLar = -1

        for ch in s:
            if ch.isdigit():
                num = int(ch)
        
                if num > larNum:
                    secondLar = larNum
                    larNum = num
                elif larNum > num > secondLar:
                    secondLar = num

        return secondLar