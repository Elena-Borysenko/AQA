import math


def square(num):
    perimetr = num * 4
    area = num * num
    diagonal = num * math.sqrt(2)
    return perimetr, area, diagonal


print(square(10))
