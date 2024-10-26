
def split_number(_number):
    digits = []
    while _number:
        digit = _number % 10
        digits.append(digit)
        print(digit)
        _number //= 10
    return digits[::-1]


number = 12345
arr = split_number(number)
print(arr)