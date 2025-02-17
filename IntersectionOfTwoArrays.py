# Time Complexity : O(mlogm + nlogn + m log n) // 2 sorting + 1 traversal * BS
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Your code here along with comments explaining your approach:
# using two pointers approach to find the common elements in both the arrays
# traversing the larger array and doing a binary search on the smaller one
# since we are moving the pointers, we will not run into duplicate elements
# but the arrays should be sorted for this approach
# if we find the required element, we move our low = found_index + 1 (to avoid duplicates)



class Solution(object):

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 is None or nums2 is None:
            return []

        m = len(nums1)
        n = len(nums2)

        if m > n:
            return self.intersect(nums2, nums1)

        # nums1 is smaller than nums2

        result = []

        nums1.sort()
        nums2.sort()

        # now we have to iterate over the smaller one:
        low = 0
        for i in range(m):
            bsIndex = self.binarySearch(nums2, low, n - 1, nums1[i])
            if bsIndex != -1:
                # binary search worked, element was found
                result.append(nums1[i])
                # so we must move our smaller element
                low = bsIndex + 1
        
        return result

    def binarySearch(self, nums, low, high, target):
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                # we need the first occurence
                # so making sure previous element is not equal to the target
                if mid == low or nums[mid-1] != target:
                    return mid
                high = mid - 1
                
            elif nums[mid] < target:
                # move right
                low = mid + 1
                
            else:
                # move left
                high = mid - 1
        
        return -1



        
