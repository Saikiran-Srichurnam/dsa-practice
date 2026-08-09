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

        maxVFreq = max(vFreq.values(), default=0)
        maxCFreq = max(cFreq.values(), default=0)

        return maxVFreq + maxCFreq