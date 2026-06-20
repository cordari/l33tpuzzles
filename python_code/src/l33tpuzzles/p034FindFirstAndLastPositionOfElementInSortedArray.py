from typing import List

"""
34. Find First and Last Position of Element in Sorted Array

Medium

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
"""
class Solution:
    """
    do two separate binary searches.
    One to look for the starting position, so it biases towards left,
    and another to look for the ending position, which biases towards right
    
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1

        # look for starting position
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: # found the target
                start = mid if (start == -1 or mid < start) else start # update the start index
                right = mid - 1 # continue to look to the left for more
            elif nums[mid] < target:
                left = mid + 1
            else: # mid > target
                right = mid - 1

        if start == -1: # if no starting index found, then it is not in the list.
            return [-1, -1]

        # look for ending position
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: # found the target
                end = mid if end == -1 or mid > end else end # update the end index
                left = mid + 1 # continue to look to the right for more
            elif nums[mid] < target:
                left = mid + 1
            else: # mid > target
                right = mid - 1

        return [start, end]
    
def main():
    nums = []
    target = 6
    sol = Solution()
    print(sol.searchRange(nums, target))

if __name__ == "__main__":
    main()

        