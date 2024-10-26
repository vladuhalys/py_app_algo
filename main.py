def to_upper(alpha: chr) -> chr:
    return chr(ord(alpha) - 32)


def to_lower(alpha: chr) -> chr:
    return chr(ord(alpha) + 32)


text = "hello, world!"
text = to_upper(text[0]) + text[1:]

print(text)
