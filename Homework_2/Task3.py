number_1 = int(input('Enter your first number'))
number_2 = int(input('Enter your second number'))
function = str(input('Enter math function:'))




if function == '+':
    print(number_1 + number_2)
elif function == '-':
    print(number_1 - number_2)
elif function == '*':
    print(number_1 * number_2)
elif function == '/':
    print(number_1 / number_2)
else:
    print('Incorrect values')
