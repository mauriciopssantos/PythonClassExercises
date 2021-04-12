#3. Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
# These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
class Validator:
    def __init__(self,parenthesesArr):
        self.parenthesesArr= parenthesesArr

    def checker(self):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in self.parenthesesArr:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

    def checker1(self):
        opening = "{[("
        closing = "}])"
        brackets = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in self.parenthesesArr:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if len(stack) == 0:
                    return False
                if stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

    def checker2(self):
        open_list = ["[","{","("]
        close_list = ["]","}",")"]
  
        stack = []
        for i in self.parenthesesArr:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack)-1])):
                    stack.pop()
                else:
                    return "Unbalanced"
        if len(stack) == 0:
            return "Balanced"
        else:
            return "Unbalanced"
    
    def checker3(self):
        open_tup = tuple('({[')
        close_tup = tuple(')}]')
        map = dict(zip(open_tup, close_tup))
        queue = []
    
        for i in self.parenthesesArr:
            if i in open_tup:
                queue.append(map[i])
            elif i in close_tup:
                if not queue or i != queue.pop():
                    return "Unbalanced"
        if not queue:
            return "Balanced"
        else:
            return "Unbalanced"

    def checker4(self):
        brackets = ['()', '{}', '[]']
        while any(x in self.parenthesesArr for x in brackets):
            for br in brackets:
                self.parenthesesArr = self.parenthesesArr.replace(br, '')
        return not self.parenthesesArr