class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        d = 0
        for i in range(len(nums1)):
            if nums1[i] == 0 and m < i + 1 :
                nums1[i] = nums2[d]
                d += 1
        nums1.sort()
        