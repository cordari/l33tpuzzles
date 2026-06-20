from typing import List
"""

53. Maximum Subarray

Medium

Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

"""

class Solution:
    """
    Kadane's algorithm, which is linear and a simple DP algorithm.

    dp[i] = maximum subarray sum ending at index i.
    because dp[i] depends on dp[i-1] only, you don't even need a dp array

    1. if the sum from the left is negative, drop that sum, you are
      better off start with the current number
    2. at each index, take the greater value between adding the current number
     to the prev sum, or take the current number alone. This by itself takes care
     of 1.
    3. also track the max, take the greater of the current max and the
      sum at i
    
    """
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        sum = nums[0]
        for i in range(1, len(nums)):
            sum = max(sum, sum + nums[i])
            best = max(best, sum) 
        return best
    
def main():
    sol = Solution()
    print(sol.maxSubArray([-1,-2,-3,-4]))

if __name__ == "__main__":
    main()

        