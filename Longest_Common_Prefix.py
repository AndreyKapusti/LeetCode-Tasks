# Task: https://leetcode.com/problems/longest-common-prefix/description/
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        longest_str = max(strs, key=len)
        strs.remove(longest_str)
        for i in range(len(longest_str)):
            for word in strs:
                if longest_str[:i+1] != word[:i+1]:
                    return longest_str[:i]
        return longest_str