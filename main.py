def _mul(items):
    mull = 1
    for i in items:
        mull *= i
    return mull


_items = [1, 2, 3, 4]
print(_mul(_items))
