'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        arr = []
        i = 0
        j = 0
        m = n1 + n2 - 1
        while i < n1 and j < n2:
            if i + j > m / 2 + 2:
                break
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        for i in range(i, n1):
            if i + j > m / 2 + 2:
                break
            arr.append(nums1[i])
        for j in range(j, n2):
            if i + j > m / 2 + 2:
                break
            arr.append(nums2[j])
        if m % 2 != 0:
            return (arr[m // 2] + arr[m // 2 + 1]) / 2
        else:
            return arr[(m - 1) // 2 + 1]


so = Solution()
nums1 = [1, 2]
nums2 = [3, 4]
print(so.findMedianSortedArrays(nums1, nums2))
