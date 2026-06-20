from typing import List, Tuple
"""

84. Largest Rectangle in Histogram

Hard

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:
             ___                         ___ 
         ___|   |                    ___|___|
        |   |   |                   | . . . |
        |   |   |    ___            | . . . |    ___
 ___    | 5 | 6 |___|   |    ___    | . 10. |___|   |
| 2 |___|   |   | 2 | 3 |   | 2 |___| . . . | 2 | 3 |
|   | 1 |   |   |   |   |   |   | 1 | . . . |   |   |

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:
     ___
    |   |
 ___| 4 |
| 2 |   |
|   |   |

     ___                 ___
    |   |               |...|
 ___|___|     OR     ___|.4.|
| . 4 . |           | 2 |...|
| . . . |           |   |...|

Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
"""

class Solution:

    """
    the algorithm uses a monotonic stack

    loop through the bar. if the bar is taller than the bar at the top of the stack, push the bar and index onto the stack. this means the shorter bars to the left of the current
    bar can be extended to the current index

    if the bar is shorter than the bar at the top of the stack, keep popping the top until the stack top bar is not taller than current bar or stack is empty

    while popping, compute the area of the bar popped, where area = height of popped bar X (current index - popped index)

    then push the current bar and start index onto the stack, where the start index would be the index of the last popped bar. This basically says for this height, it could be extended
    to the left to that start index

    after looping through the height once, the stack may not be empty. keep popping the stack until it is empty, and calculate the area for each popped off bar:
     height is the popped off height, distance is heights array size - popped index


     intuitive video https://www.youtube.com/watch?v=zx5Sw9130L0
    
    
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: List[Tuple[int, int]] = []
        max_area = 0

        for idx, curr_h in enumerate(heights):
            start = idx
            while len(stack) > 0 and stack[-1][0] > curr_h:
                bar = stack.pop()
                start = bar[1]
                area = (idx - bar[1]) * bar[0]
                max_area = max(area, max_area)
            stack.append((curr_h, start))

        while len(stack) > 0:
            bar = stack.pop()
            area = (len(heights) - bar[1]) * bar[0]
            max_area = max(area, max_area)

        return max_area


def main():
    heights = [0,1,0,1]

    sol = Solution()

    print(sol.largestRectangleArea(heights))

main()
         

