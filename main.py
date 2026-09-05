from assets import *
from random import randint
import sys
import subprocess

game_images = [ROCK, PAPER, SCISSORS]


def print_menu():
    print("*" * 18)
    print("* 0 for ROCK     *")
    print("* 1 for PAPER    *")
    print("* 2 for SCISSORS *")
    print("*" * 18)


def clear():
    command = 'cls' if sys.platform == 'win32' else 'clear'
    subprocess.run(command, shell=True)


def main():
    is_running = True

    while is_running:
        clear()
        print_menu()

        player = int(input('\nROCK, PAPER, SCISSORS, SHOOT!: '))
        print('\nYou chose:')
        print(game_images[player])

        computer = randint(0, 2)
        print('\nComputer chose:')
        print(game_images[computer])

        if player == computer:
            print('It\'s a tie!')
        elif player == 0 and computer == 2:
            print('You win!')
        elif computer == 0 and player == 2:
            print('You lose!')
        elif player > computer:
            print('You win!')
        else:
            print('Your lose!')

        is_running = input('\nPlay again (y/n): ') == 'y'


if __name__ == '__main__':
    main()
