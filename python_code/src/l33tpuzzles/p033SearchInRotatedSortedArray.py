from typing import List

"""
33. Search in Rotated Sorted Array

Medium

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4
"""
class Solution:
    """
    idea is to use binary search, use mid to split the list into two portions, and then determine which portion is sorted. And there will be 4 scenarios:
    left portion is sorted, and target is within left portion -> set right to mid - 1 and continue
    left portion is sorted, but target NOT within left portion -> set left to mid + 1 and continue
    right portion is sorted, and target is within right portion -> set left to mid + 1 and continue
    right portion is sorted, but target NOT within right portion -> set right to mid - 1 and continue
    """
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: # found
                return mid
            if left == right and nums[left] != target: # not in list
                return -1
            
            # determine if target is to the left of mid or to the right of mid
            if nums[left] <= nums[mid]: # left portion is sorted
                if nums[left] <= target and target <= nums[mid]: # target is within left portion
                    right = mid - 1
                else: # target is within right portion
                    left = mid + 1
            elif nums[mid] <= nums[right]: # right portion is sorted
                if nums[mid] <= target and target <= nums[right]: # target is within right portion
                    left = mid + 1
                else: # traget is within left portion
                    right = mid - 1
        return -1
    
def main():
    nums = [4,5,6,7,0,1,2]
    nums = [1]
    target = 0
    sol = Solution()
    print(sol.search(nums, target))

if __name__ == "__main__":
    main()

        