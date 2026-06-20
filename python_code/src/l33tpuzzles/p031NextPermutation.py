"""
31. Next Permutation

Medium

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

from typing import List


class Solution:
    """
    this problem is just to memorize the algorith. Nothing more to it.

    1. in the input, go from right to left to find the number that is followed by a number strictly greater than itself (follow meaning to its right). This number is the pivot
    2. then go from right to left again to find among the numbers to the right of the pivot the first (also the smallest) number that's strictly greater than the pivot. This number is the successor
        2A. why is the first number > pivot value also the smallest? Because this portion of the list is in descending order, guaranteed by 1.
    3. swap the pivot and the successor
    4. reverse the sublist after the pivot position

    
    """
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # find the pivot
        pivot = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                pivot = i
                break

        # find the successor
        successor = -1
        if pivot >= 0:
            for i in range(len(nums) - 1, pivot, -1):
                if nums[i] > nums[pivot]:
                    successor = i
                    break

        # swap
        if pivot >=0 and successor >= 0 and pivot != successor:
            nums[pivot], nums[successor] = nums[successor], nums[pivot]

        # reverse

        left = pivot + 1
        right = len(nums) - 1

        while (left < right):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1 
        

def main():
    sol = Solution()
    l = [1,1,5] #[3,2,1]
    sol.nextPermutation(l)
    print(l)

if __name__ == "__main__":
    main()

        