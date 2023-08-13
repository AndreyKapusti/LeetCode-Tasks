# Task: https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        if x in range(-9, 10):
            return x
        r=int((str(abs(x))[::-1]).lstrip('0'))*(-1 if x < 0 else 1)
        return r if -2147483648 <= r <= 2147483647 else 0