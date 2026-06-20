from pdb import line_prefix
from typing import List
"""
68. Text Justification

Hard

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth

"""

class Solution:
    """
    more or less straight forward algorith.
    1. grab word by word, and compute the line length. Keep the words in a list until the current word won't fit, then process the words already in the list
    2. number of spaces is 1 less than number of words in the line
    3. when calculating extra space, using diff = maxWidth - current_width to calculate the total number of extra paddings needed
    4. then diff // space_count gives the base number of ADDITIONAL spaces each space gets.
    5. then diff % space_count gives how many of these space position gets an EXTRA space more than ADDITIONAL and the base single space.
    
    """
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output: List[str] = []
        i = 0
        line_size = 0

        words_in_line: List[str] = []
        while i < len(words):
            word = words[i]
            print(f"i: {i}, word: {word}, line_size: {line_size}")
            if len(words_in_line) == 0: # put first word of line to the line always
                print("case 1")
                words_in_line.append(word)
                line_size = len(word)
                i += 1
                print(f"words_in_line: {words_in_line}, line_size: {line_size}, i: {i}")
            else:
                probe_size = len(word) + 1
                if line_size + probe_size <= maxWidth: # if next word plus space doesn't exceed max width, add word to line
                    print("case 2")
                    words_in_line.append(word)
                    line_size += probe_size
                    i += 1
                    print(f"words_in_line: {words_in_line}, line_size: {line_size}, i: {i}")
                else: # next word won't fit, must process current line
                    if len(words_in_line) == 1:  # if line has 1 word, left justify, padding spaces to end
                        print("case 3")
                        line = words_in_line[0]
                        diff = maxWidth - line_size
                        for s in range(0, diff):
                            line += " "
                        print(f"words_in_line: {words_in_line}, line_size: {line_size}, i: {i}")
                        output.append(line)
                        words_in_line.clear() # reset
                        line_size = 0
                    else:
                        print("case 4")
                        word_count = len(words_in_line)  # count number of words
                        space_count = word_count - 1 # count number of spaces, which is always 1 less than number of words
                        diff = maxWidth - line_size
                        base_space_size = diff // space_count
                        additional_spaces = diff % space_count

                        line = words_in_line[0]
                        space_position = 0
                        for w in range(1, word_count):
                            line += " "
                            for s in range(0, base_space_size):
                                line += " "
                            if space_position < additional_spaces:
                                line += " "
                            space_position += 1
                            line += words_in_line[w]
                        print(f"words_in_line: {words_in_line}, line_size: {line_size}, i: {i}")
                        output.append(line)
                        words_in_line.clear()
                        line_size = 0

        # process last line
        if len(words_in_line) > 0:
            line = words_in_line[0]
            for w in range(1, len(words_in_line)):
                line += " "
                line += words_in_line[w]
            diff = maxWidth - len(line)
            for s in range(0, diff):
                line += " "
            output.append(line)

        return output


def main():
    input = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    max = 20
    sol = Solution()
    print(sol.fullJustify(input, max))

if __name__ == "__main__":
    main()