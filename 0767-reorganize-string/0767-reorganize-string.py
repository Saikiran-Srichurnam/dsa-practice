from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []

        count = Counter(s)
        for ch, freq in count.items():
            heapq.heappush(heap, (-freq, ch))
        
        res = []

        prev_char = None
        prev_count = 0

        while heap:
            freq, ch = heapq.heappop(heap)

            res.append(ch)
            freq += 1

            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))
            
            prev_count = freq
            prev_char = ch

        if prev_count < 0:
            return ""
        
        return "".join(res)

