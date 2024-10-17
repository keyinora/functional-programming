def args_logger(*args, **kwargs):
    # Print positional arguments with numbering
    for i, arg in enumerate(args, start=1):
        print(f"{i}. {arg}")
    
    # Print keyword arguments sorted by key
    for key, value in sorted(kwargs.items()):
        print(f"* {key}: {value}")

