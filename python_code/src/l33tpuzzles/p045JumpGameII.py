from typing import List
"""
45. Jump Game II
Medium

You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].

"""

class Solution:
    def __init__(self):
        self.min_jump = 0 

    """
    the most straight-forward algorithm is using recursion, but this algorithm TIMES OUT for some cases as it is not as efficient.
    
    pass in the nums array, the idx to read, and the jump count so far. also keep a global min_jump_count
    for the value at the current index, loop i through 1 ~ value + 1.  if current idx + i reaches array size, return because it goes beyond valid index
    if the value is 0, skip, because it causes an infinite loop.

    however, the algorithm needs another optimization or it would take too long for some test cases such as [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
    the optimization is to return if the jump_count reaches the min_jump, because it won't produce the minimum number of jumps, no point doing further work

    actually it still times out for test case such as 
    [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
    
    """

    def jump_recursive(self, nums: List[int]) -> int:
        self.min_jump = len(nums) + 1  # initialize min_jump to 1 more than the length of the array as it would be the maximum
        self.jump_helper(nums, 0, 0)

        return self.min_jump
    
    def jump_helper(self, nums: List[int], idx: int, jump_count: int):
        if jump_count >= self.min_jump:
            return
        if idx == len(nums) - 1:
            self.min_jump = min(self.min_jump, jump_count)
            return
        val = nums[idx]
        
        if val == 0:
            return
        for i in range(1, val + 1):
            if idx + i >= len(nums):
                return
            self.jump_helper(nums, idx + i, jump_count + 1)

    """
    the greedy linear solution, which is kind of a BFS algorithm, and this is the recommended algorithm

    initialize 3 things:  jump count = 0, window end = 0, farthest = 0
    loop through each number from index 0 to len(nums) - 2.  We don't check the very last element as it is the destination
    update the farthest can be reached as we go through each number
    when the current index reaches end of a window, that means we have to make a jump, increment the jump count, and also update the window end to the newest farthest
    """
    def jump(self, nums: List[int]) -> int:
        jump_count = 0
        window_end = 0
        farthest = 0
        
        for i in range(0, len(nums) - 1):
            val = nums[i]
            farthest = max(farthest, i + val)
            if i == window_end:
                jump_count += 1
                window_end = farthest

        return jump_count
    
    """
    forward/bottom-up DP algorithm

    dp[i] keeps the minimal jump required to reach position i.  dp[0] is 0 because you start there. The rest would be a large number that will be replaced by the min number of jump

    outer loop progresses i from 0 to n-1, where i is the current "launch pad"

    inner loop progresses the destination that can be reached from i, and update the DP of each destination with the minimal number of jumps
    """
    def jump_dp(self, nums: List[int]) -> int:
        dp: List[List[int]] = [len(nums) + 1] * len(nums) # initialize the dp values to len(nums) + 1 as it would be a number larger than possible jumps

        dp[0] = 0

        for i in range(0, len(nums)):
            x = nums[i]
            for j in range(1, x + 1):
                if i + j >= len(nums): # can't go beyond the nums array
                    break
                jump = dp[i] + 1
                dp[i + j] = min(jump, dp[i + j])

        return dp[len(nums) - 1]
        
  


def main():
    sol = Solution()
    print(sol.jump_dp([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]))
    print(sol.jump_dp([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]))
    print(sol.jump_dp([2,3,1,1,4]))
    
    print(sol.jump_dp([2,3,0,1,4]))
    print(sol.jump_dp([2,1,1]))


if __name__ == "__main__":
    main()
