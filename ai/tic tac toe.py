board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def play():
    player = "X"
    moves = 0

    while moves < 9:
        print_board()
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1

        if board[row][col] == " ":
            board[row][col] = player
            moves += 1

            if check_winner(player):
                print_board()
                print("Player", player, "Wins!")
                return

            player = "O" if player == "X" else "X"
        else:
            print("Invalid move. Try again.")

    print_board()
    print("Draw!")

play()