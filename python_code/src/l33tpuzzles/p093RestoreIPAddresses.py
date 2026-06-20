from typing import List
"""


93. Restore IP Addresses

Medium

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

Constraints:

1 <= s.length <= 20
s consists of digits only.

"""

class Solution:
    """
    recursion + backtrack.

    the recursive helper function takes in the string, starting index, seq holding valid ip segments, and ans

    at each recursion, loop from starting index to starting index + 3 (exclusive) or len of the string
     in each iteration, substring from starting index to i
     if substring leads with 0 and substring len > 1, it is invalid, break
     otherwise, convert substring to integer. 
     if int value  > 255, invalid, break
     otherwise, check if seq already has 3 segments, if so and i is at last index of string, it completes 4, add substring to seq, join seq with ".", and add the ip string to ans;
       if i is not at last index of string, this means this last segment must take more characters, continue the loop to next iteration
    if seq doesn't have 3 segments, make recursive call, passing i+1 as the new starting index
    pop last segment from seq, so it can use a different segment for the next iteration 

    
    """
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        seq: List[str] = []
        ans: List[str] = []

        self.ip_helper(s, 0, seq, ans)

        return ans
        
    def ip_helper(self, s: str, sidx: int, seq: List[str], ans: List[str]):
        for i in range(sidx, min(sidx+3, len(s))):
            sub = s[sidx: i + 1]
            if len(sub) > 1 and sub[0] == "0":
                break
            v = int(sub)

            if v > 255:
                break

            if len(seq) == 3:
                if i == len(s) - 1:
                    seq.append(sub)
                    ans.append(".".join(seq))

                else:
                    continue
            else:
                seq.append(sub)
                self.ip_helper(s, i+1, seq, ans)
            seq.pop()
def main():
    str = "101023"

    sol = Solution()

    print(sol.restoreIpAddresses(str))

main()