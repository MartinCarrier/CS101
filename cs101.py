from random import randint, choice


class TIC_TAC_TO():
    def __init__(self):
        self.starter = False
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.computer_turn_completed = 0
        self.end_game = 0
        self.lines = [[1, 5, 9], [3, 5, 7], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9]] # 8 tic-tac-to lines
        self.print_void_board()
        self.first_question()

    def print_void_board(self):  # instructions on how to play the game
        print("\nUse this pattern to play: \n")
        print('7|8|9')
        print('-+-+-')
        print('4|5|6')
        print('-+-+-')
        print('1|2|3')
        print("\nYou get the X's, computer gets the O's\n")

    def print_board(self):  # instructions on how to play the game
        print(self.board[6] + '|' + self.board[7] + '|' + self.board[8])
        print('-+-+-')
        print(self.board[3] + '|' + self.board[4] + '|' + self.board[5])
        print('-+-+-')
        print(self.board[0] + '|' + self.board[1] + '|' + self.board[2])

    def first_question(self):  # We ask if the player wants to start or not
        temp = input('Do you want to start (Y/N)?')
        if temp == 'Y' or temp == 'y':
            self.starter = True
        else:
            self.starter = False

    def your_turn(self):  # ask the player to provide input on next move
        print('\n*************************************************')
        temp = input('Your turn, choose a number between 1 and 9: ')
        # check if it's numeric
        while temp.isnumeric() is False or int(temp) not in range(1, 10):
            temp = input('Your must enter numeric value between 1 and 9: ')

        if self.board[int(temp) - 1] == " " and int(temp) in range(1, 10):
            self.board[int(temp) - 1] = 'X'
            # return temp
        else:
            option = []
            for i in range(0,9):
                if self.board[i] == ' ':
                    option.append(i)
            index = choice(option)
            self.board[index] = 'X'
            print("Wrong input, we will choose a random choice for you......." + str(index+1))

    def validate_game_verdit(self):  # validate if we have a winner or it's a tie
        if self.board[6] == "X" and self.board[7] == 'X' and self.board[8] == 'X':
            self.end_game = 1
            return "Bravo! You won!"
        elif self.board[6] == "O" and self.board[7] == 'O' and self.board[8] == 'O':
            self.end_game = 1
            return "Sorry, you lost :("
        elif self.board[3] == "X" and self.board[4] == 'X' and self.board[5] == 'X':
            self.end_game = 1
            return "Bravo! You won!"
        elif self.board[3] == "O" and self.board[4] == 'O' and self.board[5] == 'O':
            self.end_game = 1
            return "Sorry, you lost :("
        elif self.board[0] == "X" and self.board[1] == 'X' and self.board[2] == 'X':
            self.end_game = 1
            return "Bravo! You won!"
        elif self.board[0] == "O" and self.board[1] == 'O' and self.board[2] == 'O':
            self.end_game = 1
            return "Sorry, you lost :("
        elif self.board[0] == "X" and self.board[3] == 'X' and self.board[6] == 'X':
            self.end_game = 1
            return "Bravo! You won!"
        elif self.board[0] == "O" and self.board[3] == 'O' and self.board[6] == 'O':
            self.end_game = 1
            return "Sorry, you lost :("
        elif self.board[1] == "X" and self.board[4] == 'X' and self.board[7] == 'X':
            self.end_game = 1
            return "Bravo! You won!"
        elif self.board[1] == "O" and self.board[4] == 'O' and self.board[7] == 'O':
            self.end_game = 1
            return "Sorry, you lost :("
        elif self.board[2] == "X" and self.board[5] == 'X' and self.board[8] == 'X':
            self.end_game = 1
            return "Bravo! You won!"
        elif self.board[2] == "O" and self.board[5] == 'O' and self.board[8] == 'O':
            self.end_game = 1
            return "Sorry, you lost :("
        elif self.board[0] == "X" and self.board[4] == 'X' and self.board[8] == 'X':
            self.end_game = 1
            return "Bravo! You won!"
        elif self.board[0] == "O" and self.board[4] == 'O' and self.board[8] == 'O':
            self.end_game = 1
            return "Sorry, you lost :("
        elif self.board[2] == "X" and self.board[4] == 'X' and self.board[6] == 'X':
            self.end_game = 1
            return "Bravo! You won!"
        elif self.board[2] == "O" and self.board[4] == 'O' and self.board[6] == 'O':
            self.end_game = 1
            return "Sorry, you lost :("
        elif self.board[0] == ' ' or self.board[1] == ' ' or self.board[2] == ' ' or self.board[3] == ' ' or self.board[
            4] == ' ' or self.board[5] == ' ' or self.board[6] == ' ' or self.board[7] == ' ' or self.board[8] == ' ':
            self.end_game = 0
            return "Next"
        else:
            self.end_game = 1
            return 'Tie game'

    def computer_first_turn(self):  # if computer start, random choice...
        choice = randint(0, 8)
        self.board[choice] = 'O'
        self.print_board()

    def computer_turn(self):  # computer turn
        print("\nComputer play:")
        self.computer_turn_completed = 0
        # can the computer win? If yes, close it
        self.computer_close_attack()
        # if no, can the computer lose? If yes, defend
        self.computer_defense_tactik()
        # if no, try to make a good move...
        self.computer_augment_chance()
        # if no, play safe
        self.play_safe()

    def computer_defense_tactik(self):  # give some algorithm to the computer
        # [1, 2, 3]
        if self.computer_turn_completed == 0:
            for item in self.lines:
                count = 0
                for nb in item:
                    if self.board[nb-1] == 'X':
                        count += 1
                if count == 2:
                    for nb in item:
                        if self.board[nb - 1] == ' ' and self.computer_turn_completed == 0:
                            self.board[nb - 1] = 'O'
                            self.computer_turn_completed = 1
                            break

    def computer_close_attack(self):  # offensive move, if we can win, we close!
        # first look if we can close and win
        if self.computer_turn_completed == 0:
            for line in self.lines:  # loop the lines
                count = 0
                for case in line:  # 3 cases
                    if self.board[case-1] == 'O':
                        count += 1
                if count == 2:
                    for case in line:
                        if self.board[case-1] == ' ' and self.computer_turn_completed == 0:
                            self.board[case - 1] = 'O'
                            self.computer_turn_completed = 1

    def computer_augment_chance(self):  # this function looks for a clear line with one '0'
        if self.computer_turn_completed == 0:
            for item in self.lines:
                count = 0
                for nb in item:
                    if self.board[nb-1] == 'O':
                        count += 1
                if count == 1:  # that mean we should look at this line
                    empty = 0
                    empty_case = []
                    for stuff in item:
                        if self.board[stuff-1] == " ":
                            empty_case.append(stuff)
                            empty += 1
                    if empty == 2 and self.computer_turn_completed == 0:
                        self.board[choice(empty_case)-1] = 'O'
                        self.computer_turn_completed = 1

    def play_safe(self):
        if self.computer_turn_completed == 0:
            if self.board[4] == ' ':  # play in the center
                self.board[4] = 'O'
                self.computer_turn_completed = 1
            else:
                for i in range(8, -1, -1):
                    if self.board[i] == " " and self.computer_turn_completed == 0:
                        self.board[i] = 'O'
                        self.computer_turn_completed = 1
                        break

tic = TIC_TAC_TO()
if tic.starter is False:
    tic.computer_first_turn()

while tic.end_game == 0:
    tic.your_turn()
    verdict = tic.validate_game_verdit()
    tic.print_board()
    if tic.end_game == 1:
        print(verdict)
        break
    tic.computer_turn()
    verdict = tic.validate_game_verdit()
    tic.print_board()
    if tic.end_game == 1:
        print(verdict)
        break