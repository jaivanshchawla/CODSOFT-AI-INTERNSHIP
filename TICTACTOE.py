# Tic-Tac-Toe with Mini-Max Algorithm
# Author: [Jaivansh Chawla]

def display_board(state):
    print("Current Board State:\n")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print()
        if state[i] == 0:
            print("- ", end=" ")
        elif state[i] == 1:
            print("O ", end=" ")
        elif state[i] == -1:
            print("X ", end=" ")
    print("\n")

def player_move(board):
    position = int(input("Enter X's position (1-9): ")) - 1
    if board[position] != 0:
        print("Invalid Move! Try again.")
        player_move(board)
    else:
        board[position] = -1

def computer_move(board):
    best_position = -1
    best_score = -float('inf')
    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            score = -minimax(board, -1)
            board[i] = 0
            if score > best_score:
                best_score = score
                best_position = i   
    board[best_position] = 1

def minimax(board, current_player):
    result = evaluate_board(board)
    if result != 0:
        return result * current_player
    best_score = -float('inf')
    for i in range(9):
        if board[i] == 0:
            board[i] = current_player
            score = -minimax(board, -current_player)
            board[i] = 0
            best_score = max(best_score, score)
    return best_score

def evaluate_board(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combination in winning_combinations:
        if board[combination[0]] != 0 and \
           board[combination[0]] == board[combination[1]] and \
           board[combination[0]] == board[combination[2]]:
            return board[combination[0]]
    return 0

def start_game():
    print("Computer (O) vs You (X)")
    first_player = int(input("Choose to play first (1) or second (2): "))
    board = [0] * 9
    
    for turn in range(9):
        if evaluate_board(board) != 0:
            break
        if (turn + first_player) % 2 == 0:
            computer_move(board)
        else:
            display_board(board)
            player_move(board)

    display_board(board)
    result = evaluate_board(board)
    if result == 0:
        print("It's a Draw!")
    elif result == -1:
        print("X Wins!")
    elif result == 1:
        print("O Wins!")

if __name__ == "__main__":
    start_game()