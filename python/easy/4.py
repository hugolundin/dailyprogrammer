import random

def passgen(length, use_numbers=False, use_symbols=False):
    alphabet = 'abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ'
    numbers = '0123456789'
    symbols = '!"#€%&/()=?`©@£$∞§|[]≈±´≤><'
    available = [alphabet]
    password = ''

    if use_numbers:
        available.append(numbers)

    if use_symbols:
        available.append(symbols)

    for i in range(length):
        password += random.choice(random.choice(available))

    return password
