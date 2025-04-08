def longest_unique_substring(s):
    """
    Using sliding window with variable size,
    to find the longest unique substring
    """
    max_length = 0
    seen = set()
    left = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

s = "abcabcbb"
t = longest_unique_substring(s)