import random

tic_tac_toe_board_unseen = [' ', ' ', ' ',
                            ' ', ' ', ' ',
                            ' ', ' ', ' ']

tic_tac_toe_computer_symbol = 'O'

tic_tac_toe_user_symbol = 'X'

tic_tac_toe_dictionary = {'Wins': 0, 'Losses': 0, 'Ties': 0, 'Games Played': 0}


def tic_tac_toe_game_rules():

    print()

    print('Welcome to Tic Tac Toe! Try to get your X\'s to be three in a row!')

    print()

    print('Here is the board.')

    print()

    print('1 | 2 | 3')
    print('----------')
    print('4 | 5 | 6')
    print('----------')
    print('7 | 8 | 9')

    print()

    print('The numbers correspond to the places in which you, or the computer, can put an "X" or "O".')

    print()

    print('There will be a coin toss to see who goes first.')

    print()


def tic_tac_toe_coin_toss():

    tic_tac_toe_coin = random.randint(0, 1)

    tic_tac_toe_user_coin = input('Do you pick heads or tales? ("1" for heads, "0" for tales) ')

    if (tic_tac_toe_user_coin != '0') and (tic_tac_toe_user_coin != '1'):

        print('Input either "1" for heads or "0" for tales!')

        return tic_tac_toe_coin_toss()

    elif int(tic_tac_toe_user_coin) != tic_tac_toe_coin:

        print('The computer won the coin toss!')

        tic_tac_toe_first_turn = 0

    else:

        print('You won the coin toss!')

        tic_tac_toe_first_turn = 1

    return tic_tac_toe_first_turn


def tic_tac_toe_gameplay_hub(tic_tac_toe_player_1):

    if tic_tac_toe_player_1 == 0:

        tic_tac_toe_computer_player_1()

    elif tic_tac_toe_player_1 == 1:

        tic_tac_toe_user_player_1()


def tic_tac_toe_computer_player_1():

    tic_tac_toe_computer_turns = 5

    print()

    print('The computer gets the first move.')

    print()

    while True:

        while True:

            tic_tac_toe_computer_index = random.randint(0, 8)

            if (tic_tac_toe_board_unseen[tic_tac_toe_computer_index] != 'O') and (tic_tac_toe_board_unseen[tic_tac_toe_computer_index] != 'X'):

                tic_tac_toe_board_unseen[tic_tac_toe_computer_index] = 'O'

                tic_tac_toe_computer_turns -= 1

                print('The computer placed its\' "O"!')

                print(tic_tac_toe_board_unseen[0], ' | ', tic_tac_toe_board_unseen[1], ' | ', tic_tac_toe_board_unseen[2])
                print('--------------')
                print(tic_tac_toe_board_unseen[3], ' | ', tic_tac_toe_board_unseen[4], ' | ', tic_tac_toe_board_unseen[5])
                print('--------------')
                print(tic_tac_toe_board_unseen[6], ' | ', tic_tac_toe_board_unseen[7], ' | ', tic_tac_toe_board_unseen[8])

                print()

                break

            else:

                continue

        if tic_tac_toe_board_unseen[0] == 'O' and tic_tac_toe_board_unseen[1] == 'O' and tic_tac_toe_board_unseen[2] == 'O':

            print('The computer got three in a row!')

            tic_tac_toe_dictionary['Losses'] += 1

            break

        elif tic_tac_toe_board_unseen[3] == 'O' and tic_tac_toe_board_unseen[4] == 'O' and tic_tac_toe_board_unseen[5] == 'O':

            print('The computer got three in a row!')

            tic_tac_toe_dictionary['Losses'] += 1

            break

        elif tic_tac_toe_board_unseen[6] == 'O' and tic_tac_toe_board_unseen[7] == 'O' and tic_tac_toe_board_unseen[8] == 'O':

            print('The computer got three in a row!')

            tic_tac_toe_dictionary['Losses'] += 1

            break

        elif tic_tac_toe_board_unseen[0] == 'O' and tic_tac_toe_board_unseen[3] == 'O' and tic_tac_toe_board_unseen[6] == 'O':

            print('The computer got three in a row!')

            tic_tac_toe_dictionary['Losses'] += 1

            break

        elif tic_tac_toe_board_unseen[1] == 'O' and tic_tac_toe_board_unseen[4] == 'O' and tic_tac_toe_board_unseen[7] == 'O':

            print('The computer got three in a row!')

            tic_tac_toe_dictionary['Losses'] += 1

            break

        elif tic_tac_toe_board_unseen[2] == 'O' and tic_tac_toe_board_unseen[5] == 'O' and tic_tac_toe_board_unseen[8] == 'O':

            print('The computer got three in a row!')

            tic_tac_toe_dictionary['Losses'] += 1

            break

        elif tic_tac_toe_board_unseen[0] == 'O' and tic_tac_toe_board_unseen[4] == 'O' and tic_tac_toe_board_unseen[8] == 'O':

            print('The computer got three in a row!')

            tic_tac_toe_dictionary['Losses'] += 1

            break

        elif tic_tac_toe_board_unseen[2] == 'O' and tic_tac_toe_board_unseen[4] == 'O' and tic_tac_toe_board_unseen[6] == 'O':

            print('The computer got three in a row!')

            tic_tac_toe_dictionary['Losses'] += 1

            break

        elif tic_tac_toe_computer_turns == 0:

            print('The game is a tie!')

            tic_tac_toe_dictionary['Ties'] += 1

            break

        while True:

            tic_tac_toe_user_index = input('Enter the position where you want to put your "X" (A number from 1 to 9)): ')

            if (tic_tac_toe_user_index != '1') and (tic_tac_toe_user_index != '2') and (tic_tac_toe_user_index != '3') and (tic_tac_toe_user_index != '4') and (tic_tac_toe_user_index != '5') and (tic_tac_toe_user_index != '6') and (tic_tac_toe_user_index != '7') and (tic_tac_toe_user_index != '8') and (tic_tac_toe_user_index != '9'):

                print('Please input a valid position!')

            elif tic_tac_toe_board_unseen[int(tic_tac_toe_user_index) - 1] == 'O':

                print('The computer already has an "O" in this position!')

            elif tic_tac_toe_board_unseen[int(tic_tac_toe_user_index) - 1] == 'X':

                print('You already have an "X" in this position!')

            else:

                tic_tac_toe_board_unseen[int(tic_tac_toe_user_index) - 1] = 'X'

                print('You placed your "X"!')

                print(tic_tac_toe_board_unseen[0], ' | ', tic_tac_toe_board_unseen[1], ' | ', tic_tac_toe_board_unseen[2])
                print('--------------')
                print(tic_tac_toe_board_unseen[3], ' | ', tic_tac_toe_board_unseen[4], ' | ', tic_tac_toe_board_unseen[5])
                print('--------------')
                print(tic_tac_toe_board_unseen[6], ' | ', tic_tac_toe_board_unseen[7], ' | ', tic_tac_toe_board_unseen[8])

                print()

                break

        if tic_tac_toe_board_unseen[0] == 'X' and tic_tac_toe_board_unseen[1] == 'X' and tic_tac_toe_board_unseen[2] == 'X':

            print('You got three in a row!')

            tic_tac_toe_dictionary['Wins'] += 1

            break

        elif tic_tac_toe_board_unseen[3] == 'X' and tic_tac_toe_board_unseen[4] == 'X' and tic_tac_toe_board_unseen[5] == 'X':

            print('You got three in a row!')

            tic_tac_toe_dictionary['Wins'] += 1

            break

        elif tic_tac_toe_board_unseen[6] == 'X' and tic_tac_toe_board_unseen[7] == 'X' and tic_tac_toe_board_unseen[8] == 'X':

            print('You got three in a row!')

            tic_tac_toe_dictionary['Wins'] += 1

            break

        elif tic_tac_toe_board_unseen[0] == 'X' and tic_tac_toe_board_unseen[3] == 'X' and tic_tac_toe_board_unseen[6] == 'X':

            print('You got three in a row!')

            tic_tac_toe_dictionary['Wins'] += 1

            break

        elif tic_tac_toe_board_unseen[1] == 'X' and tic_tac_toe_board_unseen[4] == 'X' and tic_tac_toe_board_unseen[7] == 'X':

            print('You got three in a row!')

            tic_tac_toe_dictionary['Wins'] += 1

            break

        elif tic_tac_toe_board_unseen[2] == 'X' and tic_tac_toe_board_unseen[5] == 'X' and tic_tac_toe_board_unseen[8] == 'X':

            print('You got three in a row!')

            tic_tac_toe_dictionary['Wins'] += 1

            break

        elif tic_tac_toe_board_unseen[0] == 'X' and tic_tac_toe_board_unseen[4] == 'X' and tic_tac_toe_board_unseen[8] == 'X':

            print('You got three in a row!')

            tic_tac_toe_dictionary['Wins'] += 1

            break

        elif tic_tac_toe_board_unseen[2] == 'X' and tic_tac_toe_board_unseen[4] == 'X' and tic_tac_toe_board_unseen[6] == 'X':

            print('You got three in a row!')

            tic_tac_toe_dictionary['Wins'] += 1

            break


def tic_tac_toe_user_player_1():

    tic_tac_toe_user_turns = 5

    print()

    print('You get the first move.')

    print()

    while True:

        while True:

            tic_tac_toe_user_index = input('Enter the position where you want to put your "X" (A number from 1 to 9)): ')

            if (tic_tac_toe_user_index != '1') and (tic_tac_toe_user_index != '2') and (tic_tac_toe_user_index != '3') and (tic_tac_toe_user_index != '4') and (tic_tac_toe_user_index != '5') and (tic_tac_toe_user_index != '6') and (tic_tac_toe_user_index != '7') and (tic_tac_toe_user_index != '8') and (tic_tac_toe_user_index != '9'):

                print('Please input a valid position!')

            elif tic_tac_toe_board_unseen[int(tic_tac_toe_user_index) - 1] == 'O':

                print('The computer already has an "O" in this position!')

            elif tic_tac_toe_board_unseen[int(tic_tac_toe_user_index) - 1] == 'X':

                print('You already have an "X" in this position!')

            else:

                tic_tac_toe_board_unseen[int(tic_tac_toe_user_index) - 1] = 'X'

                tic_tac_toe_user_turns -= 1

                print('You placed your "X"!')

                print(tic_tac_toe_board_unseen[0], ' | ', tic_tac_toe_board_unseen[1], ' | ', tic_tac_toe_board_unseen[2])
                print('--------------')
                print(tic_tac_toe_board_unseen[3], ' | ', tic_tac_toe_board_unseen[4], ' | ', tic_tac_toe_board_unseen[5])
                print('--------------')
                print(tic_tac_toe_board_unseen[6], ' | ', tic_tac_toe_board_unseen[7], ' | ', tic_tac_toe_board_unseen[8])

                print()

                break

        if tic_tac_toe_board_unseen[0] == 'X' and tic_tac_toe_board_unseen[1] == 'X' and tic_tac_toe_board_unseen[2] == 'X':

            print('You got three in a row!')

            tic_tac_toe_dictionary['Wins'] += 1

            break

        elif tic_tac_toe_board_unseen[3] == 'X' and tic_tac_toe_board_unseen[4] == 'X' and tic_tac_toe_board_unseen[5] == 'X':

            print('You got three in a row!')

            tic_tac_toe_dictionary['Wins'] += 1

            break

        elif tic_tac_toe_board_unseen[6] == 'X' and tic_tac_toe_board_unseen[7] == 'X' and tic_tac_toe_board_unseen[8] == 'X':

            print('You got three in a row!')

            tic_tac_toe_dictionary['Wins'] += 1

            break

        elif tic_tac_toe_board_unseen[0] == 'X' and tic_tac_toe_board_unseen[3] == 'X' and tic_tac_toe_board_unseen[6] == 'X':

            print('You got three in a row!')

            tic_tac_toe_dictionary['Wins'] += 1

            break

        elif tic_tac_toe_board_unseen[1] == 'X' and tic_tac_toe_board_unseen[4] == 'X' and tic_tac_toe_board_unseen[7] == 'X':

            print('You got three in a row!')

            tic_tac_toe_dictionary['Wins'] += 1

            break

        elif tic_tac_toe_board_unseen[2] == 'X' and tic_tac_toe_board_unseen[5] == 'X' and tic_tac_toe_board_unseen[8] == 'X':

            print('You got three in a row!')

            tic_tac_toe_dictionary['Wins'] += 1

            break

        elif tic_tac_toe_board_unseen[0] == 'X' and tic_tac_toe_board_unseen[4] == 'X' and tic_tac_toe_board_unseen[8] == 'X':

            print('You got three in a row!')

            tic_tac_toe_dictionary['Wins'] += 1

            break

        elif tic_tac_toe_board_unseen[2] == 'X' and tic_tac_toe_board_unseen[4] == 'X' and tic_tac_toe_board_unseen[6] == 'X':

            print('You got three in a row!')

            tic_tac_toe_dictionary['Wins'] += 1

            break

        elif tic_tac_toe_user_turns == 0:

            print('The game is a tie!')

            tic_tac_toe_dictionary['Ties'] += 1

            break

        while True:

            tic_tac_toe_computer_index = random.randint(0, 8)

            if (tic_tac_toe_board_unseen[tic_tac_toe_computer_index] != 'O') and (tic_tac_toe_board_unseen[tic_tac_toe_computer_index] != 'X'):

                tic_tac_toe_board_unseen[tic_tac_toe_computer_index] = 'O'

                print('The computer placed its\' "O"!')

                print(tic_tac_toe_board_unseen[0], ' | ', tic_tac_toe_board_unseen[1], ' | ', tic_tac_toe_board_unseen[2])
                print('--------------')
                print(tic_tac_toe_board_unseen[3], ' | ', tic_tac_toe_board_unseen[4], ' | ', tic_tac_toe_board_unseen[5])
                print('--------------')
                print(tic_tac_toe_board_unseen[6], ' | ', tic_tac_toe_board_unseen[7], ' | ', tic_tac_toe_board_unseen[8])

                print()

                break

            else:

                continue

        if tic_tac_toe_board_unseen[0] == 'O' and tic_tac_toe_board_unseen[1] == 'O' and tic_tac_toe_board_unseen[2] == 'O':

            print('The computer got three in a row!')

            tic_tac_toe_dictionary['Losses'] += 1

            break

        elif tic_tac_toe_board_unseen[3] == 'O' and tic_tac_toe_board_unseen[4] == 'O' and tic_tac_toe_board_unseen[5] == 'O':

            print('The computer got three in a row!')

            tic_tac_toe_dictionary['Losses'] += 1

            break

        elif tic_tac_toe_board_unseen[6] == 'O' and tic_tac_toe_board_unseen[7] == 'O' and tic_tac_toe_board_unseen[8] == 'O':

            print('The computer got three in a row!')

            tic_tac_toe_dictionary['Losses'] += 1

            break

        elif tic_tac_toe_board_unseen[0] == 'O' and tic_tac_toe_board_unseen[3] == 'O' and tic_tac_toe_board_unseen[6] == 'O':

            print('The computer got three in a row!')

            tic_tac_toe_dictionary['Losses'] += 1

            break

        elif tic_tac_toe_board_unseen[1] == 'O' and tic_tac_toe_board_unseen[4] == 'O' and tic_tac_toe_board_unseen[7] == 'O':

            print('The computer got three in a row!')

            tic_tac_toe_dictionary['Losses'] += 1

            break

        elif tic_tac_toe_board_unseen[2] == 'O' and tic_tac_toe_board_unseen[5] == 'O' and tic_tac_toe_board_unseen[8] == 'O':

            print('The computer got three in a row!')

            tic_tac_toe_dictionary['Losses'] += 1

            break

        elif tic_tac_toe_board_unseen[0] == 'O' and tic_tac_toe_board_unseen[4] == 'O' and tic_tac_toe_board_unseen[8] == 'O':

            print('The computer got three in a row!')

            tic_tac_toe_dictionary['Losses'] += 1

            break

        elif tic_tac_toe_board_unseen[2] == 'O' and tic_tac_toe_board_unseen[4] == 'O' and tic_tac_toe_board_unseen[6] == 'O':

            print('The computer got three in a row!')

            tic_tac_toe_dictionary['Losses'] += 1

            break


def tic_tac_toe_replay():

    print()

    print('Here\'s the scoreboard:')
    print(tic_tac_toe_dictionary)

    print()

    while True:

        tic_tac_toe_replay_input = input('Do you want to play again? ("Yes"/"No") ')

        if tic_tac_toe_replay_input.upper() == 'YES':

            print('Okay, let\'s go again!')

            tic_tac_toe_board_unseen[0] = ' '
            tic_tac_toe_board_unseen[1] = ' '
            tic_tac_toe_board_unseen[2] = ' '
            tic_tac_toe_board_unseen[3] = ' '
            tic_tac_toe_board_unseen[4] = ' '
            tic_tac_toe_board_unseen[5] = ' '
            tic_tac_toe_board_unseen[6] = ' '
            tic_tac_toe_board_unseen[7] = ' '
            tic_tac_toe_board_unseen[8] = ' '

            print()

            break

        elif tic_tac_toe_replay_input.upper() == 'NO':

            print('Okay, I\'ll see you later!')

            exit()

        else:

            print('Please input either "Yes" or "No"!')


tic_tac_toe_game_rules()

while True:

    tic_tac_toe_first_play = tic_tac_toe_coin_toss()

    tic_tac_toe_gameplay_hub(tic_tac_toe_first_play)

    tic_tac_toe_dictionary['Games Played'] += 1

    tic_tac_toe_replay()
