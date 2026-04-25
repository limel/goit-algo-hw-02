from collections import deque


def is_palindrome(string: str) -> bool:
    normalized = [c.lower() for c in string if c.isalnum()]
    chars = deque(normalized)

    while len(chars) > 1:
        left = chars.popleft()
        right = chars.pop()
        if left != right:
            return False

    return True
