from typing import List
"""
35. Search Insert Position

Easy

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""


class Solution:
    """
    do a standard binary search, i.e. loop condition is left <= right, and when splitting, left = mid + 1 or right = mid - 1.
    by the time the loop ends and if target not found, left would point to the correct insertion position

    this is because the last step that made the loop to exit would be one of the two:
    EITHER left = mid + 1.  in this case, mid was pointing at a number too small for target, and left = mid + 1 basically says the target should be after here, 
         and since it ends the loop, this is pointing at where target should be
    OR right = mid - 1. in this case, mid was pointing at a number too big for target, and right = mid - 1, basically says the target should be before here,
         but since it ends the loop, means the right is less than left, and is 1 position before where target should be.

    why is there such an asymmetry between the left and right? because when we calculate mid, we use integer division/floor, so it biases towards left, making left the
    correct index
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left