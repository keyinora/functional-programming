def create_markdown_image(alt_text):
    enclosed_alt_text = f"![{alt_text}]"

    def add_url(url):
        escaped_url = url.replace("(", "%28").replace(")", "%29")
        image_syntax = enclosed_alt_text + f"({escaped_url})"

        def add_title(title=None):
            if title:
                return image_syntax[:-1] + f' "{title}")'
            return image_syntax

        return add_title

    return add_url

