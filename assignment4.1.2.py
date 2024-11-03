def is_balanced(expression):
    stack = []
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    
    for i in expression:
        if i in matching_parentheses.values():  
            stack.append(i)
        elif i in matching_parentheses.keys():  
            if not stack or stack.pop() != matching_parentheses[i]:
                return False
    
    return len(stack) == 0


print(is_balanced("(1+2)-3*[41+6]"))  
print(is_balanced("(1+2)-3*[41+6}"))  
print(is_balanced("(1+2)-3*[41+6"))   
print(is_balanced("(1+2)-3*]41+6["))   
print(is_balanced("(1+[2-3]*4{41+6})")) 