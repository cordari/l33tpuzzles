from typing import List
"""
57. Insert Interval

Medium

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5

"""

class Solution:
    """
    no binary search needed. do a linear scan, in 3 phases

    phase 1: go through intervals, find intervals before newInterval that are not overlapping, i.e. intervals[1] < newInterval[0], and collect them into output

    phase 2: go through intervals, find intervals that overlap with newInterval, and merge into newInterval.
      when you see newInterval[1] < interval[0], you ran out of overlapping intervals. merge newInterval into output

    phase 3: go through the rest of intervals and collect them. These are intervals after newInterval that are not overlapping
    
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output: List[List[int]] = []
        
        # phase 1, collect intervals before newInterval that don't overlap
        i = 0
        while i < len(intervals):
            interval = intervals[i]
            if interval[1] < newInterval[0]:
                output.append(interval)
                i += 1
            else:
                break

        # phase 2, merge intervals that overlap with newInterval
        while i < len(intervals):
            interval = intervals[i]
            if newInterval[1] < interval[0]:
                break
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
                i += 1
        output.append(newInterval)

        # phase 3, collect the remaining intervals which are after newInterval but don't overlap
        while i < len(intervals):
            output.append(intervals[i])
            i += 1

        return output
    
def main():
    intervals = [[1,3],[6,9]]
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    intervals = [[2,5],[6,7],[8,9]]

    newInterval = [2,5]
    newInterval = [4,8]
    newInterval = [0, 1]
    sol = Solution()
    print(sol.insert(intervals, newInterval))

if __name__ == "__main__":
    main()