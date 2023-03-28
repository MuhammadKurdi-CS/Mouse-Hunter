import random                             

lives = int(input("Enter the number of attempts: "))

multiArray = [[" ","1","2","3","4","5","6","7"],
              ["1","O","O","O","O","O","O","O"],
              ["2","O","O","O","O","O","O","O"],
              ["3","O","O","O","O","O","O","O"],
              ["4","O","O","O","O","O","O","O"],
              ["5","O","O","O","O","O","O","O"],
              ["6","O","O","O","O","O","O","O"],
              ["7","O","O","O","O","O","O","O"]]

def print_board(multiArray):
    for row in multiArray:
        print(" ".join(row))

def play_game(lives):
    mouse_x = random.randint(1, 7)
    mouse_y = random.randint(1, 7)
    
    while lives > 0:
        print(f"You have {lives} lives left.")
        guess_row = int(input("Enter your row: "))
        guess_col = int(input("Enter your column: "))
        if guess_row < 1 or guess_row > 7 or guess_col < 1 or guess_col > 7:
            print("Oops, that's outside the board.")
        elif multiArray[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        elif guess_row == mouse_x and guess_col == mouse_y:
            print("Congratulations! You caught the mouse!")
            return True
        else:
            print("You missed the mouse!")
            multiArray[guess_row][guess_col] = "X"
            print_board(multiArray)
            lives -= 1
    print("Sorry, you ran out of lives. Game over.")
    return False

print_board(multiArray)
play_game(lives)