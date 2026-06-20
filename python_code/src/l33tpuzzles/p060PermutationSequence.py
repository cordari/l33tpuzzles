"""
60. Permutation Sequence

Hard

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!

"""

from typing import List


class Solution:


    """
    
    the idea is for a set of n digits [1, 2, 3, ..., n], there are n! permutations. Each digit of the set when used as the first digit of the permutation, appears (n-1)! times, because as you take
    this digit out of the set, there are (n-1) digits left, so they form (n-1)! permutations. 

    1, 2, 3, ...., n       -----
    1, 2, 3, ....               |
    ...                          ---  (n-1)!
    1, n, n-1, ..., 3, 2   -----|       

    2, 1, 3, ..., n        -----
    2, 1, 3, ...                |
    ...                         ---  (n-1)!
    2, n, n-1, ..., 3, 1   -----|
    ...

    First, make k 0-based, so k = k - 1

    So given k, you can determine the first digit by doing k // (n-1)!, which would give the index of the digit from the set/list.

    Once the first digit is nailed down, you want to know of the (n-1)! permutations, where k would land you. So that would take k % (n-1)!. This value becomes the new 0-based k,
      and with (n-1) digits, repeat the algorithm, i.e. k // (n - 2)!, gives you the index of the 2nd digit from the (n-1) set, etc.
    
    """    
    def getPermutation(self, n: int, k: int) -> str:
        zk = k - 1
        
        factorial: List[int] = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i-1] * i

        digits: List[int] = [x for x in range(1, n+1)]

        output = ""

        for i in range(0, n):
            digit_idx = zk // factorial[len(digits) - 1]
            output += str(digits[digit_idx])
            zk = zk % factorial[len(digits) - 1]
            digits = digits[: digit_idx] + digits[digit_idx + 1:]

        return output
    
def main():
    sol = Solution()
    print(sol.getPermutation(4, 9))

if __name__ == "__main__":
    main()