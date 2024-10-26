def _min(items):
    min_ = items[0]  # 5
    for i in range(1, len(items)):
        if items[i] < min_:
            min_ = items[i]
    return min_


def _max(items):
    max_ = items[0]
    for i in range(1, len(items)):
        if items[i] > max_:
            max_ = items[i]
    return max_


items_ = [5, 3, 2, 1, 4]
print(_min(items_))
print(_max(items_))
