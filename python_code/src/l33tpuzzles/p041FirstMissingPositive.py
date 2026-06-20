from typing import List

"""
41. First Missing Positive

Hard

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
"""
class Solution:
    """
    the array does NOT guarantee uniqueness of the numbers, so using Gaussian sum doesn't work. Besides, the range of the values is [integer.MIN, integer.MAX], doing sum could overflow

    the array has N elements, and we only care about positive integers, so we only care about integers between [1, N + 1]

    we can use the array itself as a hashmap, swapping existing positive value V into array index V-1, and ignore 0's and negative numbers and positive numbers that won't fit into index

    after the pass, look for element whose value is not index + 1 - that would be the missing positive integer

    if all values are in correct position, then missing number is N + 1.

    Caveats during swap:
    there are some edge cases during swap:
    1. if the number being swapped in is the same number being swapped out, advance i or it will create infinite loop
    2. if the number being swapped in is between 1 and N, inclusive, swap, but don't advance i as the new value needs to be examed
    3. if the number being swapped in is outside of 1 and N, advance i, as it has no array index to swap to
    
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            val = nums[i]
            if val > 0 and val <= n:
                if i != val - 1: # only swap when number is not already in the correct position
                    tmp = nums[val - 1]
                    nums[val - 1] = val
                    if tmp > 0 and tmp <= n and tmp != val:
                        nums[i] = tmp
                        # if swapped and new value is also between, don't advance i, because we want to 
                        # examine the new number swapped into the current position in the
                        # next iteration
                    else:
                        i += 1
                else:
                    i += 1
            else:
                i += 1 

        for i in range(0, n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1 
                

def main():
    sol = Solution()
    print(sol.firstMissingPositive([2,1]))

if __name__ == "__main__":
    main()