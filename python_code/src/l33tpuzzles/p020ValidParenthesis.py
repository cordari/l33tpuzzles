from typing import Dict, List
"""

20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        map: Dict[str, str] = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack: List[str] = []

        for p in s:
            if p == "(" or p == "[" or p == "{":
                stack.append(p)
            else:
                q = map[p]
                if len(stack) == 0 or stack[-1] != q:
                    return False
                stack.pop()
        return len(stack) == 0

def main():
    sol = Solution()
    print(sol.isValid("([)]"))

if __name__ == "__main__":
    main()