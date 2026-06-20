from typing import List, Set
"""
47. Permutations II

Medium

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

"""

class Solution:
    """
    based on standard permutation, but needs the following adjustment:
    1. sort the original list
    2. at each level, use a set to keep the pinned element that's already seen. If a pinned element is already seen, skip it.
    
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        sort_nums: List[int] = sorted(nums)
        ans = self.perm_helper(sort_nums, [])
        return ans

    
    def perm_helper(self, pre: List[int], post: List[int]) -> List[List[int]]:
        new_list = pre + post
        if len(new_list) == 1:
            return [[new_list[0]]]
        
        seen: Set[int] = set()
        ans: List[List[int]] = []
        for i in range(0, len(new_list)):
            curr = new_list[i]
            if curr not in seen:
                seen.add(curr)
                partial = self.perm_helper(new_list[:i], new_list[i+1:])
                for part in partial:
                    ans.append([curr] + part)
        return ans

def main():
    sol = Solution()
    print(sol.permuteUnique([1,2,2]))

if __name__ == "__main__":
    main()