import random
dice_numbers = list(range(2, 6+1))

while True:
    n = str(input('Input \'roll\' to throw the dice ot \'leave\' to stop the program!: '))
    chosen_number = random.choice(dice_numbers)
    if n == 'roll':
        print(' ___')
        print('|', chosen_number, '|')
        print(' ---')
        try_again = str(input('Do you want to try again? y/n: '))
        if try_again == 'y':
            continue
        elif try_again == 'n':
            print('Ok, bye')
            break
    elif n == 'leave':
        print('Ok, bye')
        break
    else:
        print('try again!')
        continue 
