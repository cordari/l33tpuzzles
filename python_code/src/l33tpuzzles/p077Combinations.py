from typing import List
"""
77. Combinations

Medium

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

Constraints:

1 <= n <= 20
1 <= k <= n

"""

class Solution:
    """
    use recursion

    at each level, loop through the passed in current number to n (including n), this is the i'th number. append the number onto the sequence.
    if sequence has k elements, copy it and append to answer;
    otherwise, recursively call the function, passing in current number + 1 as current number to the recursive call
    whether it was appended to answer, or returned from recursive call, remove the last element from sequence, so it can use the next number in the loop
    
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans: List[List[int]] = []
        seq: List[int] = []
        self.comb_helper(n, k, 1, 1, seq, ans)

        return ans

    def comb_helper(self, n: int, k: int, lvl: int, curr: int, seq: List[int], ans: List[List[int]]):
        for i in range(curr, n + 1):
            seq.append(i)
            if lvl == k:
                ans.append(seq.copy())
            else:
                self.comb_helper(n, k, lvl+1, i+1, seq, ans)
            seq.pop()

def main():
    sol = Solution()
    print(sol.combine(1,1))

main()