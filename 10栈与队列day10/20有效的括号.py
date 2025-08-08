class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                top = stack.pop()
                expected_right = dic[top]
                if expected_right != c:
                    return False
        return len(stack) == 1