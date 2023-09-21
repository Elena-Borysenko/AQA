def sum_range(start, end):

    _sum = 0

    if start > end:
        start, end = end, start

    for num in range(start, end):
        _sum += num

    return _sum


range1 = sum_range(5, 10)
range2 = sum_range(10, 5)

print('Sum numbers from 5 to 10 = ', range1)
print('Sum numbers from 10 to 5 = ', range2)

