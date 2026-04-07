"""
11. Container With Most Water


You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""
from typing import List

"""
don't use brute force which is too slow.

if using two pointers, left and right. If the point at the both ends of the array, the length of the base container would be maximum.

when moving pointers inwards, the base shrinks, so only way to have a bigger area is when the height increase.

the area is limited by the shorter of the two heights. So this means move the pointer that is the shorter of the two, and when it hits
a greater height than it has seen, check the area, and continue.

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        left_h = height[left]
        right_h = height[right]

        while left < right:
            prev_left_h = left_h
            left_h = height[left]
            prev_right_h = right_h
            right_h = height[right]

            area = (right - left) * min(left_h, right_h)
            if area > max_area:
                max_area = area
            print(f"left:{left}, h[left]: {height[left]}, right: {right}, h[right]:{height[right]}")
            if height[left] <= height[right]:
                while height[left] <= prev_left_h and left < right:
                    left += 1
                    print(f"left:{left}, h[left]: {height[left]}, pleft_h: {prev_left_h}, right: {right}, h[right]:{height[right]}, pright_h: {prev_right_h}")
            elif height[right] < height[left]:
                while height[right] <= prev_right_h and left < right:
                    right -= 1
                    print(f"left:{left}, h[left]: {height[left]}, pleft_h: {prev_left_h}, right: {right}, h[right]:{height[right]}, pright_h: {prev_right_h}")
            
        return max_area
    
def main():
    sol = Solution()
    print(sol.maxArea([1,1]))

if __name__ == "__main__":
    main()

            
        