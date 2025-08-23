# Last updated: 8/23/2025, 11:18:02 AM
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for s in strs[1:]:
            while prefix != s[:len(prefix)]:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix
        