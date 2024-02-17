from string import ascii_lowercase

ascii_lowercase += " "


def symbol_deleter(text):
    if not isinstance(text, str):
        raise ValueError
    return ''.join([i.lower() for i in text if i.lower() in ascii_lowercase])
