class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        max_freq = 0
        longest = 0

        left = 0
        for right in range(len(s)):
            # if the char present in the count (hashmap) increment it with +1 else update as 1
            count[s[right]] = count.get(s[right], 0) + 1

            max_freq = max(max_freq, count[s[right]])

            # Generally, we start index from 0 so when we want size of the window we add + 1 to the right - left 
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest



