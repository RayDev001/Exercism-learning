def color_code(color):
    for index, name in enumerate(colors()):
        if color == name:
            return index
    return None

def colors():
    return [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"
    ]