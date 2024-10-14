def reverse_string(s):
    # Base case: an empty string or single character doesn't need reversing
    if len(s) <= 1:
        return s
    # Recursive case: reverse the rest of the string and append the first character at the end
    return reverse_string(s[1:]) + s[0]
