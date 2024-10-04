import assets
from random import randint


def main():
    print(assets.MENU)

    player = int(input('ROCK, PAPER, SCISSORS, SHOOT!: '))
    print(f'\nPlayer chose: {assets.GAME_IMAGES[player]}')

    computer = randint(0, 2)
    print(f'\nComputer chose: {assets.GAME_IMAGES[computer]}')

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
