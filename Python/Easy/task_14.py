class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        min_len = min(len(s) for s in strs)
        if min_len == 0:
            return ""
        
        for i in range(min_len):
            if not all(strs[j][i] == strs[0][i] for j in range(1, len(strs))):
                return strs[0][:i]
        
        return strs[0][:min_len]
    
solution = Solution()

strs = ["ab", "a"]

result = solution.longestCommonPrefix(strs)

print(result)