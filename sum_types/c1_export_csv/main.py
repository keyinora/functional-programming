from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data):
    match(status):
        case(CSVExportStatus.PENDING):
            # Use list comprehension with map to convert all elements to strings
            # The map() function converts each element of a sublist to a string, 
            # and the list comprehension is used to apply this to each sublist, 
            # resulting in a new list of lists where all elements are strings.
            data = [list(map(str, sublist)) for sublist in data]
            return ("Pending...", data)
        case(CSVExportStatus.PROCESSING):
            # ",".join(row): Combines each list (i.e., row) into a string with 
            #  elements separated by commas.
            # "\n".join([...]): Combines all the row strings into a final string,
            #  with each row separated by a newline character.
            data = "\n".join([",".join(row) for row in data])
            return ("Processing...", data)
        case(CSVExportStatus.SUCCESS):
            return ("Success!", data)
        case(CSVExportStatus.FAILURE):
            data = [list(map(str, sublist)) for sublist in data]
            data = "\n".join([",".join(row) for row in data])
            return ("Unknown error, retrying...", data)
        case _:
            raise Exception("Unknown export status")
