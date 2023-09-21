def custom_map(callback, iterable):
    result = []
    for item in iterable:
        result.append(callback(item))
    return result


def square(x):
    return x * x


numbers = [2, 4, 10, 21]
squared_numbers = custom_map(square, numbers)
print(squared_numbers)

