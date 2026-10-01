class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen = {}

        i = 0
        j = len(numbers)
        while i < j:
            value = target - numbers[i]
            if value not in seen:
                seen[numbers[i]] = i+1
            else:
                return [seen[value] ,i+1]

            i += 1