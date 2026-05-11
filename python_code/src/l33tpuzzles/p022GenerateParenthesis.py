from typing import List

"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

"""
class Solution:

    """
    the WRONG way to think about this problem is to think of a pair of parenthesis in pairs.  i.e, given the nth pair, do I do
    ()[####], ([#])[###], ([####])? etc.  Because this would introduce duplicates, and may not exhaust combinations when n
    is large.

    Instead, of each character, which can be either "(" or ")".  

    The character can be "(" as long as the number of "(" is less than n
    The character can be ")" as long as the number of "(" is more than number of ")", and both are less than n
    When both numbers are n, it is a valid combination
    
    """
    ans: List[str] = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = [] # needed to reset the answer from previous run. it seems LeetCode instantiates 1 Solution object
        self.gen_paren(0, 0, n, "")
        return self.ans
    
    def gen_paren(self, open: int, close: int, n: int, prefix: str):
        if open == n and close == n:
            self.ans.append(prefix)
            return

        if open < n:
            self.gen_paren(open+1, close, n, prefix + "(")
        if close < n and close < open:
            self.gen_paren(open, close+1, n, prefix+")")
        
        
def main():
    sol = Solution()
    print(sol.generateParenthesis(1))

if __name__ == "__main__":
    main()

