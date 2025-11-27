class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        a=nums1+nums2
        a.sort()
        if len(a)%2==0:
            return (a[(len(a)/2)-1]+a[(len(a)/2)])/2.0
        else:
            return a[len(a)//2]
        