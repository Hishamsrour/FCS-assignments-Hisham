from collections import deque

def is_palindrome(s):
   
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    stack = []
    queue = deque()
    
    for char in s:
        stack.append(char)
        queue.append(char)
    
    while stack:
        if stack.pop() != queue.popleft():
            return False
    return True


print(is_palindrome("mom"))  
print(is_palindrome("Neveroddoreven"))  
print(is_palindrome("hello")) 