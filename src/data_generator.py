import numpy as np
import pandas as pd
import string


def generate_random_string(size, ensure_palindrome):
    letters = np.array(list(string.ascii_lowercase))

    if ensure_palindrome:
        half_size = size // 2
        half = "".join(np.random.choice(letters, size=half_size))

        if size % 2 == 0:
            return half + half[::-1]
        else:
            return half + np.random.choice(letters) + half[::-1]
    else:
        return "".join(np.random.choice(letters, size=size))


def get_random_strings(size, samples, ensure_palindrome):
    return pd.Series([generate_random_string(size, ensure_palindrome) for _ in range(samples)])


def get_random_strings_df(size, samples):
    return pd.DataFrame({"random_strings": [generate_random_string(size, True) for _ in range(samples)]})
