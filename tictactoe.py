def sum(a, b, c):

    # This function returns the sum of three numbers, which is used to check the win condition.

    return a + b + c


def printBoard(xstate, zstate):

    # This function prints the current state of the Tic Tac Toe board.
    # It checks the xstate and zstate lists to determine whether an 'X' or 'O' should be displayed,
    # or the position number if neither player has claimed that spot.

    zero = 'X' if xstate[0] else ('O' if zstate[0] else 0)
    one = 'X' if xstate[1] else ('O' if zstate[1] else 1)
    two = 'X' if xstate[2] else ('O' if zstate[2] else 2)
    three = 'X' if xstate[3] else ('O' if zstate[3] else 3)
    four = 'X' if xstate[4] else ('O' if zstate[4] else 4)
    five = 'X' if xstate[5] else ('O' if zstate[5] else 5)
    six = 'X' if xstate[6] else ('O' if zstate[6] else 6)
    seven = 'X' if xstate[7] else ('O' if zstate[7] else 7)
    eight = 'X' if xstate[8] else ('O' if zstate[8] else 8)

    # Print the board in a 3x3 grid format.

    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")


def checkWin(xstate, zstate):

    # This function checks if there is a winner.
    # It compares the player's state list (xstate or zstate) against predefined winning combinations.

    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal wins
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical wins
            [0, 4, 8], [2, 4, 6]]  # Diagonal wins


    for win in wins:

        # Check if X has won

        if sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3:
            print("X won the match!")
            return 1
        
        # Check if O has won

        if sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3:
            print("O won the match!")
            return 0
        
    # If no one has won, return -1 indicating the game continues.

    return -1


def clearBoard():

    # This function simulates clearing the console to refresh the board.
    # It prints many newlines to push the old board out of view.

    print("\n" * 100)



if __name__ == "__main__":

    # The main game loop. It continues until the player decides not to play again.

    while True:

        # Initialize the state for a new game.
        xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        turn = 1  # 1 represents X's turn, 0 represents O's turn.
        print("Welcome to Tic Tac Toe!")

        # This inner loop runs until the current game ends (someone wins or it's a draw).

        while True:

            printBoard(xstate, zstate)

            if turn == 1:

                # X's turn
                print("X's turn")
                value = int(input("Enter a value: "))
                xstate[value] = 1

            else:

                # O's turn
                print("O's turn")
                value = int(input("Enter a value: "))
                zstate[value] = 1

            # Check if there is a winner after each move.
            cwin = checkWin(xstate, zstate)

            if cwin != -1:

                # If someone has won, print the board and end the game.
                printBoard(xstate, zstate)
                print("Match Over!")

                break

            # Switch turns between X and O.

            turn = 1 - turn

        # After a game ends, ask the player if they want to play again.

        play_again = input("Do you want to play again? (y/n): ").lower()

        if play_again == 'y':

            clearBoard()  # Clear the board before starting a new game

        else:

            print("Thanks for playing!")
            
            break
