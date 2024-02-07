def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    for row in board:
        print("test")
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic-Tac-Toe! Good luck!")

    while True:
        print_board(board)
        row = int(input(f"Player {player}, enter row (1-3): ")) - 1
        col = int(input(f"Player {player}, enter column (1-3): ")) - 1

        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("That position is already taken. Try again.")
            continue

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            answer = input("Do you want to try again?")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
