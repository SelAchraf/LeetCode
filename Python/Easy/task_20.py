class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        mapping = {
            "}" : "{",
            ")" : "(",
            "]" : "[",
        }
        
        stack = []
        
        for i in s:
            if i in mapping:
                top_element = stack.pop() if stack else '#'
                if top_element != mapping[i]:
                    return False
            elif i in mapping.values():
                stack.append(i)
            else:
                print("The input must contains only this characters: '(', ')', '{', '}', '[', ']'")
                return False
        
        return not stack

solution = Solution()

input = "_"

result = solution.isValid(input)

print(result)