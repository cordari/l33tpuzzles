from typing import List

"""

56. Merge Intervals

Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
"""
class Solution:
    """
    first, sort the list of intervals by their start position
    then go through the intervals, if the next interval's start position is <= end position of current interval, merge, and update the farthest end position;
    otherwise, put the current interval in output, and start a new interval
    
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_list = sorted(intervals, key=lambda x:x[0])
        start = sorted_list[0][0]
        end = sorted_list[0][1]
        merged_intervals = []

        for i in range(1, len(sorted_list)):
            interval = sorted_list[i]
            if interval[0] <= end:
                end = max(interval[1], end)
            else:
                merged_intervals.append([start, end])
                start = interval[0]
                end = interval[1]

        merged_intervals.append([start, end])

        return merged_intervals

def main():
    sol = Solution()
    # print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(sol.merge([[4,7],[1,4]]))

if __name__ == "__main__":
    main()
