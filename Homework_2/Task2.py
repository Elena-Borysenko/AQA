v_1 = float(input('Enter first volume (l): '))
v_2 = float(input('Enter second volume (l): '))
t_1 = float(input('Enter first temperature (C): '))
t_2 = float(input('Enter second temperature (C): '))
total_volume = v_1 + v_2
total_temperature = (v_1 * t_1 + v_2 * t_2) / (v_1 + v_2)


print(f'Total volume: {total_volume:.1f} l')
print(f'Total temperature: {total_temperature:.1f} C')