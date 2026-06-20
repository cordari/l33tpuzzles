from typing import List

"""

42. Trapping Rain Water

Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""

class Solution:
    """
    solution analysis

    A. brute force: (won't implement, but helps to understand the thought progression to the actual algorithm)
    at each bar, scan left to find the max left, and scan right to find the max right. then the shorter of the left max and right max determines the possible height of the water. the
    amount of water at this bar is the shorter of the left_max and right_max minus height of the current bar. if current bar is taller, then water is 0.

    brute force is just to do this at every bar.

    B. precompute left_max's and right_max's (won't implement, but helps thought progression). we don't need to do this scan for every bar. We can precompute them with 2 linear loops. to compute left_max value of each bar, we scan
    left to right. 
    left_max[0] = bar_height[0]
    left_max[1] = max(left_max[0], bar_height[1])
    left_max[2] = max(left_max[1], bar_height[2])

    same for right_max, as it goes from right to left.

    water height at the current bar is the same as how it is computed in (A. brute force), except here it doesn't need scanning, just a look up

    C. two pointers, one point to left and one point to right. the left_max and right_max don't need to be pre-computed as they can be calculated and tracked as the two pointers move inwards. 
    
    
    """
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        total = 0
        left_max = 0
        right_max = 0

        while left <= right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)

            shorter = left_max
            current_idx = left
            move_left = True
            if height[right] < height[left]:
                shorter = right_max
                current_idx = right
                move_left = False

            current_level = max(0, shorter - height[current_idx])
            total += current_level

            if move_left:
                left += 1
            else:
                right -= 1

        return total
    
def main():
    sol = Solution()
    print(sol.trap([4,2,0,3,2,5]))

if __name__ == "__main__":
    main()

