user_string = input('Enter your text: ')

character_count = {}

for char in user_string:
    character_count[char] = character_count.get(char, 0) + 1

count_result = [f'{char}, {count}' for char, count in character_count.items()]

print(' '.join(count_result))

