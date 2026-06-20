from typing import List
"""

78. Subsets

Medium

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

class Solution:
    """
    recursion.
    add empty list to the answer first as it is always a subset
    at each recursion level, loop through passed in idx to the end of the nums. for each num at i, add it to the passed in sequence. then immediately copy the sequence as an answer and push to
    the answers list. if i hasn't reached end index, recursive call by passing in i + 1 as the new idx, and the seq.
    after the recursive call, pop the last element from seq so it can reset and have the next num at the current level
    
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = [[]]
        seq: List[int] = []
        self.sub_helper(nums, 0, seq, ans)

        return ans
        
    def sub_helper(self, nums:List[int], idx: int, seq: List[int], ans: List[List[int]]):
        for i in range(idx, len(nums)):
            curr = nums[i]
            seq.append(curr)
            ans.append(seq.copy())
            if i < len(nums) - 1:
                self.sub_helper(nums, i+1, seq, ans)
            seq.pop()
        
def main():
    sol = Solution()
    print(sol.subsets([1,2,3,4]))

main()