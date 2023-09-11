str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

print(dict(zip(map(int, str_list), map(lambda x: int(x) ** 2, str_list))))
