from enum import Enum


class EditType(Enum):
    NEWLINE = 1
    SUBSTITUTE = 2
    INSERT = 3
    DELETE = 4


def handle_edit(document, edit_type, edit):
    match edit_type:
        case EditType.SUBSTITUTE:
            return substitute(document, **edit)
        case EditType.INSERT:
            return insert(document, **edit)
        case EditType.DELETE:
            return delete(document, **edit)
        case EditType.NEWLINE:
            return newline(document, **edit)
        case _:
            raise Exception("Unknown edit type")


def newline(document, line_number):
    lines = document.split("\n")
    if len(lines) <= line_number:
        raise Exception("Invalid line number")
    line = lines[line_number]
    lines[line_number] = line + "\n"
    return "\n".join(lines)


def substitute(document, insert_text, line_number, start, end):
    lines = document.split("\n")
    if len(lines) <= line_number:
        raise Exception("Invalid line number")
    line = lines[line_number]
    if start > len(line):
        raise Exception("Invalid start index")
    if end > len(line) or end < start:
        raise Exception("Invalid end index")
    lines[line_number] = line[:start] + insert_text + line[end:]
    return "\n".join(lines)


def insert(document, insert_text, line_number, start):
    return substitute(document, insert_text, line_number, start, start)


def delete(document, line_number, start, end):
    return substitute(document, "", line_number, start, end)
