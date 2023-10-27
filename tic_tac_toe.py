# Tic-Tac-Toe Board Representation
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Define Winning Combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    # Check if the game is over and return the score
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move(board):
    best_move = -1
    best_score = -float('inf')
    for i in range(9):
        if board[i] == " ":
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Player Move
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = 'X'
                return
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number (0-8).")

# Check Winning Condition
def check_winner(board, player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Check if the Board is Full
def is_board_full(board):
    return " " not in board

# Print the Tic-Tac-Toe Board
def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("---------")

# Game Loop
while True:
    print_board(board)
    if is_board_full(board):
        print("It's a draw!")
        break

    player_move(board)
    if check_winner(board, 'X'):
        print_board(board)
        print("You win!")
        break

    best_move = ai_move(board)
    board[best_move] = 'O'
    if check_winner(board, 'O'):
        print_board(board)
        print("AI wins!")
        break
