import re

def format(text):
    # Remove anything inside parentheses (including parentheses)
    cleaned_lines = [
        re.sub(r"\([^)]*\)", "", line).strip()
        for line in text.splitlines()
    ]

    # Remove empty lines (if any)
    result = [line for line in cleaned_lines if line]

    return result

text = """
(U) R U R2' U' R2 U2' R2' U2 R U R U2 R' U2' R' U2 R
(U) R U R2' U' R2 U2' R2' U2 R U2' R' U2' R U2 R U2' R'
(U2) R U' R U2' R' U' R U2' R U2 R2' U R2 U2 R2' U R'
(U2) R U' R U2' R' U' R U2' R2 U2 R2 U R2' U2 R2 U R'
(U2) R U' R' U2 R2 U R2' U2 R U2' R U' R' U' R'
(U2) R U' R2' U2 R2' U R2 U2 R2 U2' R U' R' U' R'
(U) R U2 R U R2 U2 R2' U2 R2 U R2 U2 R' U2' R U' R'
(U2) R U2 R U R2' U2 R2 U2 R2' U R U2 R' U2' R U' R'
(U2) R U2 R' U2' R' U2 R U R U2 R2' U2' R2 U' R2' U R
(U2) R U2 R' U2' R' U2 R U2 R U R2' U' R2 U2' R2' U2 R
R U2 R2' U R2 U2 R U R' U2 R2' U' R2 U' R U' R2'
R U2 R2' U' R2' U2' R2' U2 R' U R U2 R2 U2' R' U2' R'
R U2 R2' U2' R2 U' R2' U R U' R' U2' R U2 R U2' R'
R U2 R2' U2' R2 U' R2' U R U2 R U2 R' U2' R' U2 R
(U2) R U2' R' U2 R2 U R2 U2 R2' U2 R2 U R U2 R U2' R'
(U') R' U R2 U2 R2' U R2 U2 R2 U2' R U' R' U2' R U' R
(U') R' U R2 U2 R2' U R2 U2 R2' U R' U2 R U R' U2 R2
(U') R' U R2' U2 R2 U R2' U2 R U2' R U' R' U2' R U' R
(U') R' U R2' U2 R2 U R2' U2 R2 U R' U2 R U R' U2 R2
(U2) R' U' R U2' R' U2 R U R2' U2 R2 U2 R2' U R U2 R
"""

# print(result)