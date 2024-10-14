def sum_nested_list(lst):
    total_size = 0
    for l in lst:
        if isinstance(l, list):
            total_size += sum_nested_list(l)
        else:
            total_size += l
    return total_size
