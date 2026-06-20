from typing import List
"""
81. Search in Rotated Sorted Array II

Medium

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
 

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums is guaranteed to be rotated at some pivot.
-10^4 <= target <= 10^4

"""

class Solution:
    """
    similar to search in rotated sorted array problem, the basic 4 scenarios are:
    1. left portion is sorted, i.e. nums[low] <= nums[mid]  use <= because of duplicates
      1.a  target is between nums[low] and nums[mid], search left portion
      1.b  else search right portion
    2. right portion is sorted, i.e. nums[mid] <= nums[high]
      2.a  targrt is between nums[mid] and nums[high], search right portion
      2.b  else search left portion

    however, because of duplicates, there is an additional scenario that needs to be checked first, which is
      nums[low] == nums[mid] == nums[high]

    and you don't know which portion target is in, because e.g. [4 5 1 2 3 | 4 4 4 4 4] vs [4 4 4 4 4 | 4 1 2 3 4]
    so you have to reduce the boundaries 1 by 1, i.e. low++ and high--, essentially doing a linear until it is clear 
    
    """
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if target == nums[mid]:
                return True

            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -= 1
            elif nums[low] <= nums[mid]: # left portion is sorted
                if target >= nums[low] and target < nums[mid]: # target within left portion, search left portion
                  high = mid - 1
                else:
                  low = mid + 1 # search right portion
            elif nums[mid] <= nums[high]: # right portion is sorted
                if target > nums[mid] and target <= nums[high]: # target within right portion, search right portion
                    low = mid + 1
                else:
                    high = mid - 1

        return False
    
def main():
    nums =  [2,5,6,0,0,1,2]
    target = 3
    sol = Solution()
    print(sol.search(nums, target))

main()



