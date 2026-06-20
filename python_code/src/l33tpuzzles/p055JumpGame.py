from typing import List

"""
55. Jump Game

Medium

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5

"""

class Solution:
    """
    use greedy algorithm which is linear.

    for each index, find the farthest index it can reach, and compare
    and update the overall farthest index. if at an index, farthest is
    less than the index, then it cannot be reached. if it goes through
    the entire list then it is reachable
    
    """
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(0, len(nums) - 1):
            if farthest < i:
                return False
            val = nums[i]
            reach = i + val
            farthest = max(farthest, reach)

        if farthest >= len(nums) - 1:
            return True
        
        return False
    
def main():
    sol = Solution()
    print(sol.canJump([3,2,1,0,4]))

if __name__ == "__main__":
    main()