# Last updated: 11/7/2025, 8:57:25 AM
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums        

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for n in self.nums[left:right+1]:
            sum += n
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)