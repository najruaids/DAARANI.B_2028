class Solution:
    def isValid(self, s): 
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if (c == ')' and last != '(') or \
                   (c == '}' and last != '{') or \
                   (c == ']' and last != '['):
                    return False
        return len(stack) == 0