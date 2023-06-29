# Task: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        a = len(nums1)
        if a%2 != 0:
            return nums1[(a//2)]
        else:
            return (nums1[(a//2)] + nums1[(a//2)-1])/2