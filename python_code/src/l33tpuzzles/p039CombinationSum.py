from typing import List

"""
39. Combination Sum

Medium

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""

class Solution:
    """
    the integers are positive -- although problem description says integers, the constraints indicate the integers are positive

    use recursion
    for each recursion call, pass in the candidates, the remaining sum to target, the starting index, a list tracking numbers used
       within the recursive function, loop through the candidates from the element at starting index to the end. This prevents the code to look at numbers before, preventing duplicate answers
         for each candidate, compare against the target.
         if it is the same as the target, then we found a solution. copy the elements from the chain to a new list, append the current element to the list, and append the list to the answer
         if the element is less than the target, add the element to the chain, do a recursive call, but pass a new target which is (current target - element)
         after the recursive call, don't forget to pop the element off the chain
         if the element is greater than the target, then it is not a solution, continue
    
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans:List[List[int]] = []

        chain:List[int] = []
        self.search(candidates, target, 0, chain, ans)

        return ans

    def search(self, cand: List[int], target: int, idx: int, chain: List[int], ans: List[List[int]]):
        for i in range(idx, len(cand)):
            num = cand[i]
            if num == target: # found a solution
                l = []
                for n in chain:
                    l.append(n)
                l.append(num)
                ans.append(l)
            elif num < target: # not meeting sum yet, keep going
                chain.append(num)
                self.search(cand, target - num, i, chain, ans)
                chain.pop()
            else: # num > target, exceeding the target, not a solution
                continue

def main():
    candidates = [2]
    target = 1

    sol = Solution()
    print(sol.combinationSum(candidates, target))

if __name__ == "__main__":
    main()