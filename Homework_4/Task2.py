CamelCase_list = ['FirstItem', 'FriendsList', 'MyTuple']
snake_case = []

for name in CamelCase_list:
    snake_name = ''
    for char in name:
       if char.isupper():
            snake_name += '_' + char.lower()
       else:
           snake_name += char
    snake_case.append(snake_name.strip('_'))

print(', '.join(snake_case))

