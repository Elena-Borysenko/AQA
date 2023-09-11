languages_list = {'Dart': 'Mark S. Mille',
             'JavaScript': 'Brendan Eich',
             'Kotlin': 'JetBrains',
             'C++': 'Bjarne Stroustrup'}

text = 'My favorite programming language is '
author = 'It was created by '

for languages, developers in languages_list.items():
    print(f'My favorite programming language is {languages}. It was created by {developers}')


del languages_list['Dart']
print(languages_list)
