def is_balanced(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")" and stack:
            stack.pop()
        else:
            return False
    return not stack

print(is_balanced("(())"))  # Output: True
