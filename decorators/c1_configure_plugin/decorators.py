def configure_plugin_decorator(func):
    def wrapper(*args):
        # Convert the tuples in *args to a dictionary
        kwargs = dict(args)
        # Call the original function with the dictionary as keyword arguments
        result = func(**kwargs)
        return result
    return wrapper
