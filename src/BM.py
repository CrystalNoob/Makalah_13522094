def build_last(pattern: str) -> dict[str, int]:
    last: dict[str, int] = {}
    for i in range(len(pattern)):
        last[pattern[i]] = len(pattern) - i - 1
    last[pattern[-1]] = len(pattern)
    return last


def bm_match(text: str, pattern: str) -> bool:
    last = build_last(pattern)
    if len(pattern) > len(text):
        return False
    i = len(pattern) - 1
    j = len(pattern) - 1
    pos_marker = 0
    while i <= len(text) - 1:
        if pattern[j] == text[i]:
            if j == 0:
                return True
            else:
                i -= 1
                j -= 1
        else:
            lst = last.get(text[i], len(pattern))
            pos_marker += lst
            i = pos_marker + len(pattern) - 1
            j = len(pattern) - 1
    return False
