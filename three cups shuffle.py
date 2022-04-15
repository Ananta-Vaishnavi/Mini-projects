cups = [' ', 'O', ' ']
from random import shuffle

shuffle(cups)
guess = ' '
#print(cups)

def pl_guess():
    global guess
    guess = input(
        'Go ahead make your guess (Choose a number between 1,2 and 3. ')
    while guess not in ['1', '2', '3']:
        guess = input('enter a number between 1 to 3 ')


def check_guess():
    global guess
    if (str(cups.index('O') + 1)) == guess:
        print('Congratulations!!!!!')
    else:
        print('Better luck next time')
pl_guess()
check_guess()
print('cups')
