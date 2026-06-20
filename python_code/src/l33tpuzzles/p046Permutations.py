from typing import List

"""
46. Permutations

Medium

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
class Solution:
    """
    standard permutation, using recursion.
    pass in a prefix list and postfix list
    merge the prefix and postfix lists into a new list
    if the list has only one element, terminal condition is reached, return that single element as a list of list, so it can be merged by the caller
    loop through each element of the new list to pin that element down
       during each iteration, recursive call the helper method again, pass the sublist before the pinned element as prefix, and sublist after the pinned element as post fix
       when the recursive call returns, it returns a list of lists, loop through the outer list, and merge each inner list with the pinned element, and add that merged list the answer list
    return the answer list to the caller 
    
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = self.perm_helper(nums, [])
        return ans
    
    def perm_helper(self, pre: List[int], post: List[int]) -> List[List[int]]:
        new_list = pre + post
        if len(new_list) == 1:
            return [[new_list[0]]]
        ans:List[List[int]] = []
        for i in range(0, len(new_list)):
            curr = new_list[i]
            partial = self.perm_helper(new_list[:i], new_list[i+1:])
            for part in partial:
                ans.append([curr] + part)
        return ans

def main():
    sol = Solution()
    print(sol.permute([1,2,3,4]))

if __name__ == "__main__":
    main()