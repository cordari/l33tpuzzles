"""
16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        lowest_delta = 10**5
        best_sum = 0

        pinned = 0
        while pinned < len(nums) - 2:
            left = pinned + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[pinned] + nums[left] + nums[right]
                delta = sum - target
                if abs(delta) < abs(lowest_delta):
                    lowest_delta = delta
                    best_sum = sum
                if delta == 0:
                    return sum
                elif delta < 0:
                    left += 1
                elif delta > 0:
                    right -= 1
            pinned += 1

        return best_sum
    
def main():
    sol = Solution()
    print(sol.threeSumClosest([1,1,1,1], -100))

if __name__ == "__main__":
    main()

