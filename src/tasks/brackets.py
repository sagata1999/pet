def validate_brackets(s: str) -> bool:
    stack = []

    allowed_brackets = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in allowed_brackets.values():
            stack.append(char)

        elif char in allowed_brackets:
            if not stack or stack[-1] != allowed_brackets[char]:
                return False

            stack.pop()
        else:
            continue

    return len(stack) == 0

a = ")(())()()()"
print(validate_brackets(a))