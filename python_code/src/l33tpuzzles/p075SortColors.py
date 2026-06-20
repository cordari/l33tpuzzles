from typing import List

"""

75. Sort Colors

Medium

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""
class Solution:
    """
    because the values of the array can only be 0, 1, or 2, the sort can be achieved using a one-pass, known as Dutch Flag algorithm.

    Keep two pointers, left, and right.  anything to the left of left pointer should be 0s and anything to the right of right pointer should be 2.

    have a probe pointer go through the elements, and exchange with left or right if value is 0 or 2. when exchange is made, advance left or decrement right.  don't increment probe because it needs to 
    exam the value that was exchanged.

    advance probe is the value is 1;  if value 0 and probe is same as left, advance.  if value is 2 and probe is same or beyond right, break


    
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        probe = 0

        while probe < len(nums):
            val = nums[probe]
            if val == 0:
                if probe > left:
                    nums[probe] = nums[left]
                    nums[left] = 0
                    left += 1
                else:
                    probe += 1
            elif val == 2:
                if probe < right:
                    nums[probe] = nums[right]
                    nums[right] = 2
                    right -= 1
                else:
                    break
            else:
                probe += 1

def main():
    nums = [2,2,2,2,2]
    sol = Solution()
    sol.sortColors(nums)
    print(nums)

main()