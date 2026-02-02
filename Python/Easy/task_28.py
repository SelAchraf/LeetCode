class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
                
        legnth_needle = len(str(needle))
        length_haystack = len(str(haystack))
        
        for i in range(length_haystack - legnth_needle + 1):
            if haystack[i:i + legnth_needle] == needle:
                return i
        return -1

solution = Solution()
haystack = "hello"
needle = "ll"
result = solution.strStr(haystack, needle)
print(result)