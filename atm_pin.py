pin = 1234
counter = 0
while counter < 3:
    pin_entry = input('Please enter your PIN: ')
    try:
        if int(pin_entry) == pin:
            print('\nYour account balance is: 0. Goodbye!')
            break
    except ValueError:
        pass
    print('Invalid pin')
    counter += 1
    if counter == 3:
        print("\nAccount locked. The police are on the way.")
