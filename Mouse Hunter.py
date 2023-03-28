import random # importing the random module from The Python Standard Library. 

""" 
Reference: https://www.youtube.com/watch?v=7Ki_2gr0rsE - CodeCademy - "Learn Python with CodeCademy: Battleship!"
           CodingTutorials360, Published on 12 Sep 2015
           https://stackoverflow.com/questions/44552249/how-to-make-a-life-meter-using-a-while-loop-in-python
           https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html
           
           
This code will allow a user to hunt a mouse using x and y coordinates on a 2 dimensional array (grid).
The user can input their guess by entering the row and column, in till they catch the mouse.

"""
lives = 0 
lives = int(input("Enter your attempts: ")) # the user can input the number of lives he or she wishes

multiArray = [[" ","1","2","3","4","5","6","7"],  #the is initialised array by array
              ["1","O","O","O","O","O","O","O"],
              ["2","O","O","O","O","O","O","O"],
              ["3","O","O","O","O","O","O","O"],
              ["4","O","O","0","O","O","O","O"],
              ["5","O","O","O","O","O","O","O"],
              ["6","O","O","O","O","O","O","O"],
              ["7","O","O","O","O","O","O","O"]]

def Board(multiArray): #the function is dedicated to looping the row in the grid and printing the grid  
    for Row in multiArray:
        print(" ".join(Row))

Board(multiArray)   # grid is printed as the function is called. 

randomMouseX = random.randint(1, 7) # this will generate a random X coordinate for the mouse in the grid bewteen 1 and 7
randomMouseY = random.randint(1, 7) # this will generate a random Y coordinate for the mouse in the grid bewteen 1 and 7


while lives !=0: # the while loop will iterate lives in the game
    guessRow = int(input("Enter your row: ")) #asking the user to input row and column 
    guessCol = int(input("Enter your column: "))
    
    """
    These if statements will ensure the users inputs are correct on the grid, if the user meets the correct requirements
    inform the user the mouse is caught. Else if the user inputs incorrect coordinates that is outside the grid 
    inform them. Else if check if the user has already input the same coordinates. 
    Lastly inform the user if he or she missed the mouse on the grid. 
    
    The CodeCademy video has enabled me to understand the concept of this code. 
    
    """
       
    if guessRow == randomMouseX and guessCol == randomMouseY: #x and y coordinates equal to random mouse coordinates
        print('congrats you caught the mouse')
        quit() # leave the game if mouse caught
        
    elif (guessRow < 0 or guessRow > 7) or (guessCol < 0 or guessCol > 7): # if user inputs less than 0, inform their guesses is ouside the grid, same if it's greater than 7 
        print("Outside the grid.")
        lives = lives -1   
    elif(multiArray[guessRow][guessCol] == "X"):  
        print("You guessed that one already.")
        lives = lives -1
    else:
        print("You missed the mouse!")
        multiArray[guessRow][guessCol] = "X"
        
        print(lives, " lives left ") # print the user's lives.
        lives = lives -1
              
        Board(multiArray)
        
    if lives <1:
          print("Game Over, you run out of lives")  