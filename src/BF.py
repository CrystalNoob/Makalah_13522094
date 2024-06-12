# String matching with brute force algorithm
def bruteforce(text: str, pattern: str) -> bool:
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return True
    return False
