from typing import Dict, List, Tuple

"""

49. Group Anagrams

Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
class Solution:
    """
    the critical part is to decide on how the keys should be represented.

    It is straight forward to go through each word, and compute the frequency count of each letter, but how to transform that info into a valid key is the critical part.

    in python, there are two ways. one is to sort the letters of the word and form the key as a string, another is to use a 26-element list to keep letter count, and then convert it to tuple
    
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection: Dict[Tuple, List[str]] = {}
        origin = ord("a")
        for word in strs:
            count: List[int] = [0] * 26
            for l in word:
                idx = ord(l) - origin
                count[idx] += 1
            key = tuple(count)
            if key in collection:
                collection[key].append(word)
            else:
                collection[key] = [word]
        ans = []
        for key in collection.keys():
            ans.append(collection[key])
        return ans

def main():
    sol = Solution()
    # print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(sol.groupAnagrams(["a"]))

if __name__ == "__main__":
    main()
