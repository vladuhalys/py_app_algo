def _sum(items):
    summ = 0
    for item in items:
        summ += item
    return summ


def _avg(items):
    return _sum(items) / len(items)


items = [1, 2, 3, 4, 5]
print(_sum(items))
print(_avg(items))
