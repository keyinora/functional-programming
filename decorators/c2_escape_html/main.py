def replacer(old, new):
    def replace(decorated_func):
        def wrapper(text):
            # Replace instances of old with new in the text
            modified_text = text.replace(old, new)
            # Pass the modified text to the decorated function
            return decorated_func(modified_text)
        return wrapper
    return replace

# Apply a series of decorators for HTML escape sequences
@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text):
    return f"<pre>{text}</pre>"
