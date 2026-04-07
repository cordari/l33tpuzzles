
from typing import List

"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

"""

"""
 idea is simple: go through the list, for each number, find the diff from the target sum, and see if the diff is
 already seen by keeping a map from value -> list index. if found, then the current number and that seen value 
 satisfies.  If not seen, just put the current number and its index in the list and move on.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_ind_dict: dict[int, int] = {}

        for i, val in enumerate(nums):
            delta: int = target - val
            if delta in val_to_ind_dict:
                return [i, val_to_ind_dict[delta]]
            val_to_ind_dict[val] = i

        return [-1, -1]

