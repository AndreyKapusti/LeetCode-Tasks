# Task: https://leetcode.com/problems/4sum/
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        for a in nums:
            for b in nums[1::]:
                for c in nums[2::]:
                    for d in nums[3::]:
                        if a+b+c+d == target:
                            to_add = [a, b, c, d]
                            to_add.sort()

                            if to_add not in output:
                                output.append(to_add)
                            else:
                                pass
        return output