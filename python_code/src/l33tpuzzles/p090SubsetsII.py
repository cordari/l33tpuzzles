from typing import List, Set
"""
90. Subsets II

Medium

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""

class Solution:
    """
    similar to Subset, except 
    1. first sort the nums
    2. at each recursive call level, keep a set of numbers already seen. if the number is already seen, skip

    initialize answer with an empty list as an element, as it is always in a subset

    pass in the sorted nums, the starting index, the sequence of numbers collected so far, and the ans

    at each recursive call, loop from the passed in idx to the end of the list

    for each number, if it is already in the seen set, skip

    otherwise, append the number to the sequence, copy the sequence as an element to the answer list. if the current iteration index (not the passed-in starting index) is not reaching end of the list,
    make a recursive call by passing in starting index to be current index + 1

    whether the recursive call was made or not, after it, remove the last element from sequence to make room for the next element in the list at the same recursion level
    
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        numsorted = sorted(nums)
        ans: List[List[int]] = [[]]
        seq: List[int] = []

        self.sub_helper(numsorted, 0, seq, ans)

        return ans
    
    def sub_helper(self, ns: List[int], idx: int, seq: List[int], ans: List[List[int]]):
        seen: Set[int] = set()
        for i in range(idx, len(ns)):
            n = ns[i]
            if n in seen:
                continue
            seen.add(n)
            seq.append(n)
            ans.append(seq.copy())
            if i + 1 < len(ns):
                self.sub_helper(ns, i + 1, seq, ans)
            seq.pop()

def main():
    nums = [0]
    sol = Solution()
    print(sol.subsetsWithDup(nums))

main()