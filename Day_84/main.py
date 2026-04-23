class AlreadyFilled(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


arrXO = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
BOARD = ''
END_GAME = False


def update_board():
    global BOARD
    BOARD = (
        '     0   1   2 \n'
        f' 0   {arrXO[0][0]} | {arrXO[0][1]} | {arrXO[0][2]}\n'
        '    -----------\n'
        f' 1   {arrXO[1][0]} | {arrXO[1][1]} | {arrXO[1][2]}\n'
        '    -----------\n'
        f' 2   {arrXO[2][0]} | {arrXO[2][1]} | {arrXO[2][2]}\n'
    )


def check_win():
    # Rows and Columns
    for i in range(3):
        if arrXO[i][0] != ' ' and arrXO[i][0] == arrXO[i][1] == arrXO[i][2]:
            return True
        if arrXO[0][i] != ' ' and arrXO[0][i] == arrXO[1][i] == arrXO[2][i]:
            return True

    # Diagonals
    if arrXO[0][0] != ' ' and arrXO[0][0] == arrXO[1][1] == arrXO[2][2]:
        return True
    if arrXO[0][2] != ' ' and arrXO[0][2] == arrXO[1][1] == arrXO[2][0]:
        return True

    return False

player1 = input("Choose your sign by typing 'X' or 'O': ").strip().upper()
player2 = 'O' if player1 == 'X' else 'X'
curr_player = player1

update_board()
print(BOARD)

while not END_GAME:
    try:
        coords_input = input(f'[{curr_player} turn] Choose coords (e.g., 1,1): ')
        row, col = map(int, coords_input.split(','))

        # Check if coordinates are within the 3x3 grid
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("OUT OF BOUNDS! Use 0, 1, or 2.")
            continue

        if arrXO[row][col] == " ":
            arrXO[row][col] = curr_player
        else:
            raise AlreadyFilled("THIS IS ALREADY FILLED!")

        update_board()
        print(BOARD)

        # Check for winner
        if check_win():
            print(f'The winner is: {curr_player}!')
            END_GAME = True
        # Check for draw
        elif not any(' ' in row for row in arrXO):
            print('DRAW! The board is full.')
            END_GAME = True
        else:
            # Switch players only if no win/draw
            curr_player = player2 if curr_player == player1 else player1

    except AlreadyFilled as e:
        print(e)
    except (ValueError, IndexError):
        print("WRONG FORMAT! You should put something like: 0,0\n")