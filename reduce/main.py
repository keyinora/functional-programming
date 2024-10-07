import functools


def join(doc_so_far, sentence):
    # Concatenate the accumulator with the new sentence, adding a period and a space in between
    return f"{doc_so_far}. {sentence}"

def join_first_sentences(sentences, n):
    # If n is 0, return an empty string
    if n == 0:
        return ""
    
    # Slice the list to get the first n sentences
    first_n_sentences = sentences[:n]
    
    # Use reduce to join the first n sentences
    result = functools.reduce(join, first_n_sentences)
    
    # Add the final period at the end
    return result + "."
