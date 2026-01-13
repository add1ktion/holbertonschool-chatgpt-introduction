#!/usr/bin/python3
"""
Tic-Tac-Toe Game - Complete Implementation
Two-player 3x3 grid game with full error handling and draw detection.
Players alternate X/O placement aiming for 3-in-a-row victory.
"""

def print_board(board):
    """
    Display current game board with proper formatting.
    
    Args:
        board (list): 3x3 list of lists containing "X", "O", or " "
    """
    print("   0   1   2 ")
    print("─────────────")
    for i, row in enumerate(board):
        print(f"{i}  ", end="")
        print(" | ".join(row), end="")
        print("  ")
        print("─────────────")

def check_winner(board):
    """
    Check for winning condition (row/col/diag) and return winner symbol.
    
    Args:
        board (list): Current 3x3 game board
        
    Returns:
        str or None: "X", "O", or None (no winner)
    """
    # Rows
    for row in board:
        if row[0] != " " and row[0] == row[1] == row[2]:
            return row[0]
    # Columns  
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    # Diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def is_board_full(board):
    """
    Check if board has no empty spaces (draw condition).
    
    Args:
        board (list): Current 3x3 game board
        
    Returns:
        bool: True if full, False otherwise
    """
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """
    Main game loop with comprehensive input validation.
    Handles ValueError, bounds checking, occupied cells.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print("Enter row (0,1,2) and column (0,1,2)")
    
    while True:
        print_board(board)
        
        # Check win condition
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} WINS!")
            break
            
        # Check draw
        if is_board_full(board):
            print_board(board)
            print("It's a DRAW!")
            break
            
        # Input validation loop
        while True:
            try:
                row = int(input(f"\nPlayer {player} - Row (0,1,2): "))
                col = int(input(f"Player {player} - Col (0,1,2): "))
                
                # Bounds check
                if row not in [0, 1, 2] or col not in [0, 1, 2]:
                    print("Invalid! Use 0, 1, or 2 only.")
                    continue
                
                # Occupied cell check
                if board[row][col] != " ":
                    print("Spot taken! Choose empty cell.")
                    continue
                
                # Valid move
                board[row][col] = player
                player = "O" if player == "X" else "X"
                break
                
            except ValueError:
                print("Invalid input! Enter numbers 0, 1, or 2.")

if __name__ == "__main__":
    """
    Program entry point.
    """
    tic_tac_toe()
