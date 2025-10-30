# Last updated: 10/30/2025, 9:05:18 AM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, i, r = 0, 0, len(nums) - 1;

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j];
            nums[j] = tmp
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l+=1
            if nums[i] == 2:
                swap(i, r)
                r-=1
                i-=1
            i+=1

        