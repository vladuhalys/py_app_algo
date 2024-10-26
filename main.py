def binary_search(_items, _key):
    _low = 0
    _high = len(_items) - 1
    while _low <= _high:
        _mid = (_low + _high) // 2
        _guess = _items[_mid]
        if _guess == _key:
            return _mid
        if _guess > _key:
            _high = _mid - 1
        else:
            _low = _mid + 1
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))