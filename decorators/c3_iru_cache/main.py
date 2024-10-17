# ?
from functools import lru_cache
# ?
@lru_cache()
def is_palindrome(word):
    if len(word) <= 1:
        return True
    # If the outermost characters are not the same, it's not a palindrome
    if word[0] != word[-1]:
        return False
    # Recursive case: check the word excluding the first and last characters
    return is_palindrome(word[1:-1])
