class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        res = []

        stack.append(nums2[0])
        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = nums2[i]
            
            stack.append(nums2[i])
        
        while stack:
            next_greater[stack.pop()] = -1
        
        for num in nums1:
            res.append(next_greater[num])

        return res

            