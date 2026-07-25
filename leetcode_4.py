class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # check for larger arrary size and perform swap if required 

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        low = 0
        high = m

        # while look and then find partcision 
        while low<=high:
            
            p1 = low + high // 2
            p2 = (m+n+1) // 2 - p1


        # calculate the value of min max of each partician 

        l1 = float('-inf') if p1 == 0 else nums1[p1-1]
        r1 = float('inf') if p1 == m else nums[p1]

        l2 = float('-inf') if p2 == 0 else nums[p2-1]
        r2 = float('inf') if p2 == n else nums[p2]

        # check for validition 

        if l1 <= r2 and l2 <= r1:

            if (m+n) % 2 == 0:
                # even
                return (max(l1, l2) +
                            min(r1, r2)) / 2.0
            # odd
            return max(l1, l2)

        elif l1 > r1:
                high = p1 - 1

            else:
                low = p1 + 1









        




        
