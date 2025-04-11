from collections import deque
import pandas as pd

### Iterative ###
# Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n)


def is_palindrome_iterative(s):
    i, j = 0, len(s) - 1  # O(1)

    while i < j:
        # print(str(s[i]) + " "  + str(s[j]))  # O(n)
        if s[i] != s[j]:  # O(1)
            return False
        i += 1  # O(1)
        j -= 1  # O(1)
    return True


#### Reverse ###
# Complexity:
#  - Best Case: O(n)
#  - Average Case: O(n)
#  - Worst Case: O(n)
def is_palindrome_reverse(s):
    return s == s[::-1]  # O(n)


### Recursive ###
# Complexity:
#   - Best Case: O(1) -> if the first and last characters are not the same
#   - Average Case: O(n)
#   - Worst Case: O(n)


def is_palindrome_recursive(s):
    if len(s) < 2:  # O(1)
        return True
    if s[0] != s[-1]:  # O(1)
        return False
    return is_palindrome_recursive(s[1:-1])  # O(n)


### Join Reverse ###
# Complexity:
#  - Best Case: O(1) -> if the first and last characters are not the same
#  - Average Case: O(n)
#  - Worst Case: O(n)


def is_palindrome_join_reverse(s):
    rev = "".join(reversed(s))  # O(n)

    if s == rev:  # O(1)
        return True  # O(1)
    return False  # O(1)


### Stack and Queue ###
# Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n)


def is_palindrome_stack_queue(s):
    stack = []  # O(1)
    queue = deque()  # O(1)

    for char in s:  # O(n)
        stack.append(char)  # O(1)
        queue.append(char)  # O(1)

    while stack:  # O(n)
        if stack.pop() != queue.popleft():  # O(1)
            return False  # O(1)
    return True  # O(1)
