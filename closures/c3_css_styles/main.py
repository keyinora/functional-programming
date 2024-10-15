def css_styles(initial_styles):
    styles = initial_styles.copy()

    def add_style(selector, property, value):
        nonlocal styles
        if selector in styles:
            styles[selector][property] = value
        else:
            styles[selector] = {property: value}
        return styles
    return add_style
