def printBoard(xstate, zstate):

    zero = 'X' if xstate[0] else ('O' if zstate[0] else 0)
    one = 'X' if xstate[1] else ('O' if zstate[1] else 1)
    two = 'X' if xstate[2] else ('O' if zstate[2] else 2)
    three = 'X' if xstate[3] else ('O' if zstate[3] else 3)
    four = 'X' if xstate[4] else ('O' if zstate[4] else 4)
    five = 'X' if xstate[5] else ('O' if zstate[5] else 5)
    six = 'X' if xstate[6] else ('O' if zstate[6] else 6)
    seven = 'X' if xstate[7] else ('O' if zstate[7] else 7)
    eight = 'X' if xstate[8] else ('O' if zstate[8] else 8)

    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")


if __name__ == "__main__":

    while True:

        xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        turn = 1  # 1 for X and 0 for O
        print("Welcome to Tic Tac Toe!")

        while True:

            printBoard(xstate, zstate)

            if turn == 1:

                print("X's turn")

                value = int(input("Enter a value: "))
                
                xstate[value] = 1

            else:

                print("O's turn")

                value = int(input("Enter a value: "))
                
                zstate[value] = 1