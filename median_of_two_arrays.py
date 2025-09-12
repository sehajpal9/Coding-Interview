# given two array, return the median of the two sorted arrays 
# for example: nums1 = [1,2,3], nums2 = [4,3] 
# merged and sorted arrays would be [1, 2, 3, 3, 4]
# median of the merged sorted array would be 3

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)
        combined_size = m + n
        median_index = combined_size / 2.00

        merged = nums1 + nums2
        #print(merged)

        merged.sort()
        #print(merged)

        # if the length of the combined list is an even number
        if combined_size % 2 == 0:
            return (merged[int(median_index - 1)] + merged[int(median_index)]) / 2

        return merged[int(median_index)]
