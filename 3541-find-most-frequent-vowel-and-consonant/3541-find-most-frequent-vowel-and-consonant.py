class Solution:
    def maxFreqSum(self, s: str) -> int:
        vFreq = {}
        cFreq = {}

        for ch in s:
            if ch in "aeiou":
                if ch in vFreq:
                    vFreq[ch] += 1
                else:
                    vFreq[ch] = 1
            else:
                if ch in cFreq:
                    cFreq[ch] += 1
                else:
                    cFreq[ch] = 1

        maxVFreq = 0
        for value in vFreq.values():
            maxVFreq = max(vFreq.values())

        maxCFreq = 0
        for values in cFreq.values():
            maxCFreq = max(cFreq.values())

        total = maxCFreq + maxVFreq
        return total