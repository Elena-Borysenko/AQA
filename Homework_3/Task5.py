IP_address = input('Enter IP address: ')
ip = IP_address.split('.')

if len(ip) == 4:
    is_valid = True

    for part in ip:
        if not part.isdigit() or not (0 <= int(part) <= 255):
           is_valid = False


    if is_valid:
        print('Your IP is correct')
    else:
        print('IP is incorrect')


