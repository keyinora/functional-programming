from functools import reduce


def paginator(page_length):
    def paginate(document):
        words = document.split()

        def add_word_to_pages(pages, word):
            if not pages:  # If no pages yet, start with the word
                return [word]
            
            current_page = pages[-1]  # Last page is the current page
            if len(current_page) + len(word) + 1 <= page_length:  # +1 accounts for the space
                pages[-1] = current_page + " " + word  # Add word to the current page
            else:
                pages.append(word)  # Start a new page with the word
            return pages

        return reduce(add_word_to_pages, words, [])

    return paginate
