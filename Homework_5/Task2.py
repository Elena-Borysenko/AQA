class FormulaError (Exception):
    pass


class WrongOperatorError (Exception):
    pass


counter = 3
while counter != 0:
    try:
        user_data = input('Enter a formula consisting of a number, an operator'
                          ' and another number separated by a space (f.e. 2 * 5): ')
        parts = user_data.split()
        num_1 = float(parts[0])
        num_2 = float(parts[2])
        operator = parts[1]

        if len(parts) < 3:
            raise FormulaError('You are entered less than 3 elements')
        elif operator not in ('*', '/'):
            raise WrongOperatorError('You entered wrong math operator')

        if operator == '/':
            result = num_1 / num_2
            print(result)
            break
        elif operator == '*':
            result = num_1 * num_2
            print(result)
            break

    except ValueError:
        print('You must entered only numbers')
    except ZeroDivisionError:
        print('Division by zero')

    counter -= 1

    if counter == 0:
         print('You entered wrong values for 3 times')


