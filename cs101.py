from random import randint


class TIC_TAC_TO():
    def __init__(self):
        self.starter = False
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.end_game = 0
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
        if self.board[int(temp) - 1] == " " and int(temp) in range(1, 10):
            self.board[int(temp) - 1] = 'X'
            # return temp
        else:
            print("Wrong input")

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
        for i in range(0, 9):
            if self.board[i] == " ":
                self.board[i] = 'O'
                break

    def computer_tactik(self):  #give some algorithm to the computer
        pass


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