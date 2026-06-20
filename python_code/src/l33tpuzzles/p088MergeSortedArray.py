from typing import List
"""
88. Merge Sorted Array

Easy

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[j] <= 10^9
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?

"""

class Solution:
    """
    because nums1 has n extra room in the back of the array, we can merge and copy the numbers from the end.

    the insertion pointer starts at the end of the nums1 array, two probe pointers both start at the end of valid portion of nums1 and end of nums2
    which ever number is larger, it is copied to the insertion pointer. advance insertion pointer and the probe pointer that was moved.  keep doing that as long as both 
    probe pointers are not negative

    after the loop, whichever probe pointer is not negative, just iterate through the rest of that array and insert.
    
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        insert_ptr = m + n - 1

        nums1_ptr = m - 1
        nums2_ptr = n - 1

        while nums1_ptr >= 0 and nums2_ptr >= 0:
            x = nums1[nums1_ptr]
            y = nums2[nums2_ptr]
            if x >= y:
                nums1[insert_ptr] = x
                nums1_ptr -= 1
            else:
                nums1[insert_ptr] = y
                nums2_ptr -= 1
            insert_ptr -= 1


        if nums1_ptr >= 0:
            for i in range(nums1_ptr, -1, -1):
                nums1[insert_ptr] = nums1[i]
                insert_ptr -= 1

        elif nums2_ptr >= 0:
            for i in range(nums2_ptr, -1, -1):
                nums1[insert_ptr] = nums2[i]
                insert_ptr -= 1

def main():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1

    sol = Solution()
    sol.merge(nums1, m, nums2, n)

    print(nums1)

main()
