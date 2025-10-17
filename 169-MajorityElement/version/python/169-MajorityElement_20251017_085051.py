# Last updated: 10/17/2025, 8:50:51 AM
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        res, maxCount = 0, 0
        for num in nums:
            count[num] = count.get(num, 0) + 1
            res = num if count[num] > maxCount  else res
            maxCount = max(count[num], maxCount)
        return res
        