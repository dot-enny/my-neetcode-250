# Last updated: 8/22/2025, 12:48:37 AM
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
        