# Last updated: 7/7/2026, 1:53:08 PM
1class Solution:
2    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
3        l, r = 0, k
4        for c in arr[k:]:
5            if abs(c - x) < abs(arr[l] - x):
6                l, r = l + 1, r + 1
7            elif abs(c - x) == abs(arr[l] - x) and arr[l] == c:
8                l, r = l + 1, r + 1
9        return arr[l:r]