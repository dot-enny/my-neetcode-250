# Last updated: 1/7/2026, 3:22:01 PM
1class Solution(object):
2    def checkIfExist(self, arr):
3        """
4        :type arr: List[int]
5        :rtype: bool
6        """
7        seen = {}
8        for i in range(len(arr)):
9            if arr[i]*2 in seen:
10                return True
11            if (arr[i] % 2 == 0) and (arr[i] // 2) in seen:
12                return True
13            seen[arr[i]] = i
14        return False
15        