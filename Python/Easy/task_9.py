class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        number_str = str(x)
        if number_str[0:] == number_str[::-1]:
            return True
        else:
            return False
    
solution = Solution()

x = 10

result = solution.isPalindrome(x)
if result:
    print("Yes it is a palindrome")
else:
    print("No it is not a palindrome")