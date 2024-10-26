def mode_split(_text, _pattern):
    for char in pattern:
        _text = _text.replace(char, '')
    return _text.split()


def mode_split_with_lower(_text, _pattern):
    _text = _text.lower()
    for char in pattern:
        _text = _text.replace(char, '')
    return _text.split()


text = "No description, website, or topics provided."
pattern = '.,!?@#$%^&*()_+'

words = mode_split_with_lower(text, pattern)
print(words)
