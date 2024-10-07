def remove_invalid_lines(document):
    return '\n'.join(filter(lambda line: '-' not in line, document.split("\n")))
