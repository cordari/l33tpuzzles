"""
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
"""

from typing import List


class Solution:
    """
    This problem requires both unique answers and unique indices, while the unique answers reqirement could be easily overlooked as it is hidden
    in the problem description.

    So once that's clear, the problem is similar to the 3Sum, but because of the unique answers requirement, it needs to skip over the same
    number that's already seen.

    sort the list and keep a pointer to pin down the first number.
    keep another pointer to pin down the second number.
    keep a left and right pointer for the 3rd and 4th numbers, and move these pointers based on the sum.
    
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        first = 0
        answers = []
        while first < len(nums) - 3:
            second = first + 1
            while second < len(nums) - 2:
                third = second + 1
                fourth = len(nums) - 1
                while third < fourth:
                    sum = nums[first] + nums[second] + nums[third] + nums[fourth]
                    if sum == target:
                        answers.append([nums[first], nums[second], nums[third], nums[fourth]])
                        third += 1
                        while third < fourth and nums[third] == nums[third - 1]:
                            third += 1
                    elif sum < target:
                        third += 1
                        while third < fourth and nums[third] == nums[third - 1]:
                            third += 1
                    elif sum > target:
                        fourth -= 1
                        while third < fourth and nums[fourth] == nums[fourth + 1]:
                            fourth -= 1
                second += 1

                while second < len(nums) and nums[second] == nums[second - 1]:
                    second += 1

            first += 1
            while first < len(nums) and nums[first] == nums[first - 1]:
                first += 1
        return answers
    
def main():
    sol = Solution()
    print(sol.fourSum([2,2,2,2,2], 8))

if __name__ == "__main__":
    main()

