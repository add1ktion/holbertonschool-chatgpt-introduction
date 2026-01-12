#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] != " " and row[0] == row[1] == row[2]:
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    # Check diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            print("Player {} wins!".format(winner))
            break
        if is_board_full(board):
            print("It's a draw!")
            break
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2) for player {}: ".format(player)))
                col = int(input("Enter column (0, 1, or 2) for player {}: ".format(player)))
                if row not in [0, 1, 2] or col not in [0, 1, 2]:
                    print("Coordinates must be 0, 1, or 2. Try again.")
                    continue
                if board[row][col] == " ":
                    board[row][col] = player
                    player = "O" if player == "X" else "X"
                    break
                else:
                    print("That spot is already taken! Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers 0, 1, or 2.")

tic_tac_toe()
