from random import randint


def main():
    print('''
================================
|      ROCK PAPER SCISSORS     |
================================
|       '0' for Rock           |
|       '1' for Paper          |
|       '2' for Scissors       |
================================
''')

    player = int(input('ROCK, PAPER, SCISSORS, SHOOT!: '))
    print(f'Player chose: {player}')

    computer = randint(0, 2)
    print(f'Computer chose: {computer}')

    if player == computer:
        print('It\'s a tie!')
    elif player == 0 and computer == 2:
        print('You win!')
    elif computer == 0 and player == 2:
        print('You lose!')
    elif player > computer:
        print('You win!')
    else:
        print('You lose!')


if __name__ == '__main__':
    main()
