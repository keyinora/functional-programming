def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        # Convert *args using convert_md_to_txt
        new_args = list(map(convert_md_to_txt, args))
        
        # Convert **kwargs values using convert_md_to_txt, keeping the keys
        new_kwargs = {k: convert_md_to_txt(v) for k, v in kwargs.items()}
        
        # Call the original function with the modified arguments
        return func(*new_args, **new_kwargs)
    
    return wrapper



# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)

