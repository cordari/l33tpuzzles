

from typing import Dict, List

"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

2 -> abc
3 -> def
4 -> ghi
5 -> jkl
6 -> mno
7 -> pqrs
8 -> tuv
9 -> wxyz
 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

"""
class Solution:
    mapping: Dict[str, str] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
    def letterCombinations(self, digits: str) -> List[str]:
        return self.getCombo(0, digits)
        


    def getCombo(self, idx: int, digits: str) -> List[str]:
        if idx >= len(digits):
            return [""]
        ans = []
        combo = self.mapping[digits[idx]]
        sub_combo = self.getCombo(idx + 1, digits)
        for ltr in combo:
            for comb in sub_combo:
                ans.append(ltr + comb)
        return ans

def main():
    sol = Solution()
    print(sol.letterCombinations("2"))

if __name__ == "__main__":
    main()