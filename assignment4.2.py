def decodeMessage (message):
    stack = []

    for i in message:
        if i != '*':
            stack.append(i)
        else:
            if stack:
                stack.pop()
    return ''.join(stack)

print(decodeMessage(" ******* SIVLE ****** DAED TNSI *** "))