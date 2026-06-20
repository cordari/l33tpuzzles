from typing import List, Set
"""
40. Combination Sum II

Medium

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

"""

class Solution:
    """
    1. sort the list, because problem demands non-duplicate combinations
    2. use recursion, pass in the sorted list, the target number to sum to, the current index of the sorted list, a chain list to track the numbers already used, and the answers list.
       within each recursion call, keep a local set of numbers that's already used at the current recursion level. 
       loop through the passed in sorted list, from the passed-in index to the end. skip numbers that are already in that local set to prevent duplicate answers.
       check the passed in target against the current number.
       if they match, it is a solution. create a new list with whatever's in chain, append the current number, and add to the answers list
       if number is less than target, there is potential. recursive call again, with index incremented, chain with current number appended, and new target with current number deducted. when the recursion call
       ends, pop that number from the chain to reset
       if number is greater than target, then it is not possible to be answer, nor will any numbers after (because list is sorted). end the current call

    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_cand = sorted(candidates)
        ans: List[List[int]] = []
        chain: List[int] = []

        self.search(sorted_cand, target, 0, chain, ans)

        return ans

    def search(self, cand: List[int], target: int, idx: int, chain: List[int], ans: List[List[int]]):
        seen: Set[int] = set()
        for i in range(idx, len(cand)):
            num = cand[i]
            if num in seen: # skip duplicate numbers at the same recursion level, to prevent duplicate answers
                continue
            seen.add(num)
            if num == target: # found an answer
                l = []
                for n in chain:
                    l.append(n)
                l.append(num)
                ans.append(l)
            elif num < target: # possible solution, keep going
                chain.append(num)
                self.search(cand, target - num, i + 1, chain, ans) # i + 1 as each number may only be used once
                chain.pop()
            else: # num > target, not posible
                return 
            
            
def main():
    cand = [10,1,2,7,6,1,5]
    cand = [2,5,2,1,2]
    target = 8
    target = 5

    sol = Solution()
    print(sol.combinationSum2(cand, target))

if __name__ == "__main__":
    main()
