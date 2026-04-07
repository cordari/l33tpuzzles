from typing import List

"""
4. Median of Two Sorted Arrays

HARD!!!!

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6

"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        # linear solution O(m+n). Need to do O(log(m + n)) using binary search
        total_size = len(nums1) + len(nums2)
        high_ind = total_size // 2
        low_ind = total_size // 2 - 1 if total_size % 2  == 0 else total_size // 2

        merged_ind = 0
        med_first_val = 0
        med_second_val = 0

        ind1 = 0
        ind2 = 0

        l1_ended = len(nums1) == 0
        l2_ended = len(nums2) == 0

        merged_val = 0

        done = False
        
        while not done:
            if not l1_ended:
                if not l2_ended:
                    if nums1[ind1] <= nums2[ind2]:
                        merged_val = nums1[ind1]
                        ind1 = ind1 + 1
                        if ind1 >= len(nums1):
                            l1_ended = True
                    else:
                        merged_val = nums2[ind2]
                        ind2 = ind2 + 1
                        if ind2 >= len(nums2):
                            l2_ended = True
                    merged_ind = merged_ind + 1
                else:
                    merged_val = nums1[ind1]
                    ind1 = ind1 + 1
                    if ind1 >= len(nums1):
                        l1_ended = True
                    merged_ind = merged_ind + 1
            elif not l2_ended:
                merged_val = nums2[ind2]
                ind2 = ind2 + 1
                if ind2 >= len(nums2):
                    l2_ended = True
                merged_ind = merged_ind + 1
            else:
                done = True

            if merged_ind - 1 == low_ind:
                if low_ind == high_ind:
                    med_first_val = merged_val
                    med_second_val = merged_val
                    done = True
                else:
                    med_first_val = merged_val
            elif merged_ind - 1 == high_ind:
                med_second_val = merged_val
                done = True

        return (med_first_val + med_second_val) / 2
        """

        # O(log(m+n)) binary search solution
        # the idea is like this: to find the median of the combined list, is essentially to find a cut off point in the combined list where the left and right partitions have equal number
        # of elements (or one has 1 more when size is odd), but more importantly, all elements in the left cannot be greater than any elements in the right.  The 2nd condition is true
        # no matter where the cut is in a sorted list, but it is important for two separate lists.
        # because we have two separate lists, both are sorted, so the problem boils down to finding the correct cut off points in both lists so that the left portitions from both lists have
        # elements no greater than anything from right poritions from both lists

        list1: List[int] = nums1
        list2: List[int] = nums2

        len1 = len(list1)
        len2 = len(list2)

        # ensure first list is the shorter one. only need to do binary search on the shorter list
        if len1 > len2:
            list1, list2 = list2, list1
            len1, len2 = len2, len1

        left = 0
        right = len1

        

        while left <= right:
            # use binary search to determine partition cut off point of the shorter list
            # (low + high) // 2 is how to calculate the binary search midpoint
            list1_part = (left + right) // 2

            # list 2 partition cut off point would dynamically be determined based on list one partition cut off point
            # note: the left partition needs to include the extra element when list size is odd, thus (len1 + len2 + 1) // 2, which gives the right answe for odd and even list size
            # note: conceptually, (len1 + len2 + 1) // 2 is not offset, but the number of elements in the left portion of the combined list, and minus the list1_part gives the 
            # parititon cut off index without list 2
            list2_part = (len1 + len2 + 1) // 2 - list1_part

            # get the list1's left partition max value. because list is sorted, the max value is the element before
            # the list 1 partition cut off point. if cut off point is the first element of the list, use -inf as a
            # sentry value
            l1_left_max = float("-inf") if list1_part == 0 else list1[list1_part - 1]

            # get list1's right partition min value, which is the element at the partition cut off point, unless the
            # cut off is the end of the list (all elements of list1 are in left partition, no element in right partition),
            # then use inf as a sentry value
            l1_right_min = float("inf") if list1_part == len1 else list1[list1_part]

            # similarly find list2's left partition max value and right partition min value
            l2_left_max = float("-inf") if list2_part == 0 else list2[list2_part - 1]
            l2_right_min = float("inf") if list2_part == len2 else list2[list2_part]

            # need to make sure all values in the left partitions are no larger than all values in the right partitions
            # since both lists are sorted, only need to do cross-list compare

            if l1_left_max > l2_right_min:
                # if left partition of list1 has value greater than right partition of list2, then list1 cut off
                # point needs to move to the left
                right = list1_part - 1
            elif l2_left_max > l1_right_min:
                # if right partition of list1 has value less than left partition of list2, then list1 cut off
                # point needs to move to the right
                left = list1_part + 1
            else:
                # both lists are partitioned correctly, it is time to figure out the median based on combined
                # list size is even or odd

                if (len1 + len2) % 2 == 1:
                    # when it is odd, the median would be the max value of the left partition of the combined list.
                    # so beween the two lists, the bigger of the left max is the median
                    return float(max(l1_left_max, l2_left_max))
                else:
                    # when it is even, median is average of max val from left parition in combined list and min val
                    # from right partition in combined list.
                    return float(max(l1_left_max, l2_left_max) + min(l1_right_min, l2_right_min)) / 2
                




        

        


