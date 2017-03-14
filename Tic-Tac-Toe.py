####################################################################
# alkharaan-zimmer-proj07
#
# CPS 201 project #07
# Mohammd Alkharaaan - Jeffrey Zimmer
#
# designed to create Oh-No-Tic-Tac-Toe game to solve project #07.
#
# algorithm:
#   create a name header function and play now function for proper
#       spacing
#   create function to create a playing board (list of lists)
#   create function to print out board using create board function
#   create function to check for valid user input and reprompt if
#       necessary, also try-except block if integer not entered
#   create function for 2 player or computer opponent with a try-
#       except block for valid input
#   create function for player choice and who begins first with a 
#       try-except block for valid input(including already selected
#       squares)
#   create function for player move and reprint board
#   create function for computer move(?)
#   create function to check for winner in rows, columns &
#       diagonally, tie game, or no winner
#   call functions to print headers,prompt for board size,create
#       and print board,type of player,and who goes first
#   call function for player moves and/or computer moves
#   call function to check for winner after each move
#
#   Missing requirement: Had alot of trouble with column winner
#       it does not always calculate winner correctly, but out of
#       time and patience, Sunday 8 p.m.
#
#   Missing requirement: after 'Lets Play', does not print board
#      prior to prompting for move as the spec sheet output shows.
####################################################################

def name_header():
    
    ''' Prints the name of the game with required spaces attached
        used to simply save space in the main program block
    '''
    
    print('Welcome to Oh-No-Tac-Toe!')
    print('Game Design: Zimmer & AlKharaan')
    print()

def play_header():

    '''Prints "Let's Play" with the required spaces attached
       used to simply save space in the main program block
    '''
    
    print()
    print('Let\'s Play!')
    print()
    
def valid_input():
    
    '''Takes in no arguments. prompts for user input and if input
       less than 3 and greater than 10, it re-prompts and returns
       user_input. Also reprompts if an integer is not entered by
       using a try-except construct
    '''

    control_variable = False
    while control_variable == False:
        try:
            user_input = int(input('How many rows and cols? '))
            while user_input < 3 or user_input > 10:
                print('rows and cols must be between (3-10)')
                user_input = int(input('How many rows and cols? '))
            control_variable = True

        except ValueError:
            print('you must enter an integer')
            
    # end of while loop
    
    return user_input

def create_board(user_input):
    
    '''Creates a create_board (list of lists) using user input to
       determine amount of elements in lists and amount of lists in
       create_board, uses '-' to denote every element inside list
    '''

    rows = []
    board_list = []
    for number in range(0,user_input):
        rows.append('-')
        board_list.append(rows)
        
    # end for loop
    
    return board_list
        
def print_board(print_board):

    '''Uses create_board function to properly print out a Oh-No-Tic
       -Tac-Toe board
    '''

    for each_row in print_board:
        for each_col in each_row:
            print(each_col, " ", end="")
        print()
        
    # end for loop
    
    return print_board

def convert_to_tuple(old_list):

    '''Used to convert list coming out of a function to a tuple to
       avoid scope problems
    '''

    new_list = []
    for element in old_list:
        new_list.append(tuple(element))

    new_tuple = tuple(new_list)
    
    # end for loop
    
    return new_tuple

def convert_to_list(board):
    
    ''' user to convert the board into list
    '''
    
    temp_board = []                     
    for element in game_board:          
        temp_board.append(list(element))
        
    # end for loop
    
    return temp_board

def human_or_machine():

    '''prompts for choice between human or computer opponent. returns
       a 1 or a 2. also includes try-except constuct for valid input
    '''

    control_variable = False
    while control_variable == False:
        
        try:
            type_player = int(input('play 2 player(1) or computer'\
                                    '(2)?: '))
            if type_player == 1 or type_player == 2:
                control_variable = True
            
        except ValueError:
            print('you must enter a (1) or a (2)')
            
    # end while loop
    
    return type_player
    

def select_player():
    
    '''Simply selects which player goes first. takes in no arguments
       prompts within the function. reprompts if a (1) or (2) is not
       entered by using a try-except construct
    '''
    
    control_variable = False
    while control_variable == False:
        
        try:
            player = int(input('Select X player(1) or O player(2): '))
            if player == 1 or player == 2:
                control_variable = True
            
        except ValueError:
            print('you must enter a (1) or a (2)')
            
    # end while loop
    
    return player

def two_player_game(player):

    '''Function that creates and runs game play for human vs.
       human gameplay. takes input from user and adds the
       appropriate symbol to the list to be used to create
       the updated game board
    '''
    
    control_variable = False
    while control_variable == False:
        try:
            if player == 1:         

                move = input('X moves? (e.g. X,Y): ')
                move = move.split(',')
                new_row = int(move[0])
                new_column = int(move[1])
                if temp_board[new_row][new_column] != 'X'\
                   and temp_board[new_row][new_column] != 'O':
                    temp_board[new_row][new_column] = 'X'
                    control_variable = True
                       
            else:

                move = input('O moves? (e.g. X,Y): ')
                move = move.split(',')
                new_row = int(move[0])
                new_column = int(move[1])
                if temp_board[new_row][new_column] != 'X'\
                    and temp_board[new_row][new_column] != 'O':
                    temp_board[new_row][new_column] = 'O'
                    control_variable = True

        except ValueError:
            print('You must enter an index number in the form X,Y')
        except IndexError:
            print('You must enter an index number between (0,{})'\
                  .format(user_input-1))
            
    # end while loop
            
def computer_play(player,user_input):

    '''Function that creates and runs game play for human vs.
       computer gameplay. takes input from user and adds the
       appropriate symbol to the list. Also adds computer choice
       using random number generator to be used to create the
       updated game board
    '''   

    import random
    control_variable = False
    while control_variable == False:
        try:
            if player == 1:         

                move = input('X moves? (e.g. X,Y): ')
                move = move.split(',')
                new_row = int(move[0])
                new_column = int(move[1])
                if temp_board[new_row][new_column] != 'X'\
                   and temp_board[new_row][new_column] != 'O':
                    temp_board[new_row][new_column] = 'X'
                    control_variable = True
                                               
            else:

                new_row = random.randrange(user_input)
                new_column = random.randrange(user_input)
                print('Computer moves {},{}'.format\
                      (new_row,new_column))
                if temp_board[new_row][new_column] != 'X'\
                   and temp_board[new_row][new_column] != 'O':
                    temp_board[new_row][new_column] = 'O'
                    control_variable = True

        except ValueError:
            print('You must enter an index number in the form X,Y')
            print()
        except IndexError:
            print('Enter a number inside the range of 0,{}'\
                  .format(user_input-1))
            print()
            
    # end while loop
    
def row_winner(board, user_input):
    
       ''' This function is to check the rows for a winner
           return True or False
       '''
       
       for i in range(user_input):
            for row in board:
                for ele in row:
                       if row[i] != 'O' and ele =='X':
                              if 'O' not in row and '-' not in row:
                                  return True
                       elif row[i] != 'X' and ele =='O':
                              if 'X' not in row and '-' not in row:
                                  return False
                                
        # end for loop

def col_winner(board, user_input):
    
       ''' This function takes the board and user input
           as parameters, and appends the columns to a list
           and check the list to announce the winner
       '''
       
       new_list = []
       x_count = 0
       o_count = 0
       for i in range(user_input):
              new_list.append(board[i][1:-1])
              if 'X'  in new_list[i]:
                     x_count += 1
                     if x_count == user_input:
                            return True
              if 'O' in new_list[i]:
                     o_count += 1
                     if o_count == user_input:
                            return False
        # end for loop
        
def first_col_winner(board, user_input):
    
       ''' This function takes the board and user input
           as parameters, and appends the first col to a list
           and check the list to announce the winner
       '''
       
       new_list = []
       for i in range(user_input):
              new_list.append(board[i][0])
              if 'O' not in new_list and '-' not in new_list:
                     if len(new_list) == user_input:
                            return True
              if 'X' not in new_list and '-' not in new_list:
                     if len(new_list) == user_input:
                            return False

        # end for loop
                                   
def last_col_winner(board, user_input):
    
       ''' This function takes the board and user input
           as parameters, and appends the last col to a list
           and check the last col to announce the winner
       '''
       
       new_list = []
       for i in range(user_input):
              new_list.append(board[i][-1])
              if 'O' not in new_list and '-' not in new_list:
                     if len(new_list) == user_input:
                            return True
              if 'X' not in new_list and '-' not in new_list:
                     if len(new_list) == user_input:
                            return False
        # end for loop

def winner(board, user_input):
    
      ''' This function determines the winner
          takes the board and user_input as parameters
          returns a boolean statement
      '''
      
      new_list = []
      for i in range(user_input):
          new_list.append(board[i][i])
          if 'O' not in new_list and '-' not in new_list:
              if len(new_list) == user_input:
                  return True
              if 'X' not in new_list and '-' not in new_list:
                  if len(new_list) == user_input:
                      return False
                    
        # end for loop
                        
def rev_winner(board, user_input):
    
       ''' This function to determine the winner, in reverse
           takes board and user_input as parameters.
           return a boolean statement.
       '''
       
       new_list = []
       win_list = []
       for i in range(user_input):
           new_list.append(board[i][::-1])
           win_list.append(new_list[i][i])
           if 'O' not in win_list and '-' not in win_list:
                  if len(win_list) == user_input:
                         return True
           if 'X' not in win_list and '-' not in win_list:
                  if len(win_list) == user_input:
                         return False

def switch_player(player):

    '''Simply switches players. used to solve a scope problem
       to send into either game function
    '''
    
    if player == 1:
        player = 2
    else:
        player = 1

    return player

def space():
    
    '''Created this to add a more human-readable element to the main
       program block
    '''

    print()

def is_board_full(board, user_input):
    
    ''' Function to check the board for blanks
        returns False if still - in board
    '''
    
    for i in range(user_input):
            for element in board:
                if element[i] == '-':
                    return True

def con_playing():
    
    ''' This function is created to continue playing to call the
        functions and make the main program looks more tight.
    '''
    
    if row_winner(game_board, user_input) == True:
        return True
    elif row_winner(game_board, user_input) == False:
        return False
    elif first_col_winner(game_board, user_input) == True:
        return True
    elif first_col_winner(game_board, user_input) == False:
        return False
    elif last_col_winner(game_board, user_input) == True:
        return True
    elif last_col_winner(game_board, user_input) == False:
        return False
    elif winner(game_board, user_input) == True:
        return True
    elif winner(game_board, user_input) == False:
        return False
    elif rev_winner(game_board, user_input) == True:
        return  True
    elif rev_winner(game_board, user_input) == False:
        return False
    elif not is_board_full(game_board, user_input) == True:
        return 'Tie'
    elif col_winner(game_board, user_input) == True:
        return True
    elif col_winner(game_board, user_input) == False:
        return False


######################## Main Program ##############################

name_header()
user_input = valid_input()        
play_header()
game_board = print_board(convert_to_tuple(create_board(user_input)))
space()
type_game = human_or_machine()
space()

if type_game == 1:      # Chooses Human vs. Human game play

    game = True
    player = select_player()
    
    while game != False:
        temp_board = convert_to_list(game_board)        
        two_player_game(player)
        game_board = convert_to_tuple(temp_board)
        space()
        print_board(game_board)
        player = switch_player(player)
        con_playing()
        if con_playing() == True:
            print('X wins the game!!')
            break
        if con_playing() == False:
            print('O wins the game!!')
            break
        if con_playing() == 'Tie':
            print('it is a Tie')
            break

    # end while loop
        
if type_game == 2:      # Chooses Human vs. Computer game play

    game = True
    player = 1
    
    while game != False:
        temp_board = convert_to_list(game_board)
        computer_play(player,user_input)
        game_board = convert_to_tuple(temp_board)
        space()    
        print_board(game_board)
        player = switch_player(player)
        con_playing()
        if con_playing() == True:
            print('X wins the game!!')
            break
        if con_playing() == False:
            print('O wins the game!!')
            break
        if con_playing() == 'Tie':
            print('it is a Tie! !')
            break

    # end while loop
        
            


