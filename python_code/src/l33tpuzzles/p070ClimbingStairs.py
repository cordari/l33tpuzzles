from typing import List
"""
70. Climbing Stairs

Easy

Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

"""

class Solution:
    """
    straight-forward DP

    DP[x] is the number of ways to reach step X

    DP[0] = 1 because you start there

    loop i through 0 ~ n-1

    at each i, the number of ways to reach i + 1 is the number of ways
    to reach i, plus the existing ways reaching i + 1

    at each i, the number of ways to reach i + 2 is the number of ways
    to reach i, plus the existing ways reaching i + 2

    given i + 1 and i + 2 don't exceed array boundary.

    array has n+1 elements, so DP[n] has number of ways to reach top
    
    """
    def climbStairs(self, n: int) -> int:
        dp: List[int] = [0] * (n + 1)

        dp[0] = 1

        for i in range(0, n):
            idx_1 = i + 1
            idx_2 = i + 2

            if (idx_1 <= n):
                dp[idx_1] = dp[i] + dp[idx_1]
            if (idx_2 <= n):
                dp[idx_2] = dp[i] + dp[idx_2]

        return dp[n]
    
def main():
    sol = Solution()
    print(sol.climbStairs(3))

if __name__ == "__main__":
    main()


