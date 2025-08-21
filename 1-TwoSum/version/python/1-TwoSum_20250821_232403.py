# Last updated: 8/21/2025, 11:24:03 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diffCheck = {};
        result = [];
        for i, n in enumerate(nums):
            difference = target - n;
            if difference in diffCheck:
                return [diffCheck[difference], i];
            diffCheck[n] = i;
        return []
        