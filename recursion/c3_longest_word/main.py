def find_longest_word(document, longest_word=""):
    # Base case: if the document is empty or only contains spaces
    if not document.strip():
        return longest_word
    
    # Split the document into the first word and the rest
    words = document.split(maxsplit=1)  # Split into at most two parts: first word and the rest
    first_word = words[0]
    rest_of_document = words[1] if len(words) > 1 else ""
    
    # Update longest_word if the current first word is longer
    if len(first_word) > len(longest_word):
        longest_word = first_word
    
    # Recursive call with the rest of the document
    return find_longest_word(rest_of_document, longest_word)

