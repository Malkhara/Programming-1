####################################################################
# alkharaan-zimmer-proj03
#
# CPS 201 project #03
# Mohammd Alkharaaan - Jeffrey Zimmer
#
# designed to play rock, paper, scissors(CPS-201 project 3 solution)
#
# algorithm
#   import random number generator
#   print welcome statement
#   get computer choice and display
#   player makes rounds choice
#   force rounds input
#   loop for amount of rounds required
#   computer makes choice
#   player makes choice
#   force player choice
#   resolve computer choice and player choice
#   count wins, losses and draws and display
#   create play again loop
#   ending display
####################################################################

import random

print('Welcome to Rock, Paper, Scissors')
print('Authors: Alkharaan and Zimmer')
print()

play_again = "y"

while play_again == 'y':
    rounds_int = int(input('How many rounds would you like to play '
                           'in a game? '))

    #force rounds choice

    while (rounds_int > 10 or rounds_int < 1):
        print("I'm sorry, but you must choose between 1 and 10 rounds.")
        rounds_int = int(input('How many rounds would you like to '
                               'play in a game? '))

    count = 1
    UserWin_int = 0
    CompWin_int = 0
    ties_int = 0


    while count <= rounds_int:
        choice = random.randint(1 , 3)

        print()
        print('Round # ', count)

        print("I've made my choice.")

        user_choice = input('Please choose: (r)ock, (p)aper, (s)cissors: ')

    #force user choice

        while (user_choice != 'r') and (user_choice != 'p') and \
                (user_choice != 's'):
            print('Invalid choice...try again.')
            user_choice = input('Please choose: (r)ock, (p)aper, '
                             '(s)cissors: ')

    #Conflict resolution

        if (choice == 1) and (user_choice == 'p'):
            print('Me: rock, You: paper. You win !')
            UserWin_int = UserWin_int + 1
        elif (choice == 1) and (user_choice == 's'):
            print('Me: rock, You: scissors I win !')
            CompWin_int = CompWin_int + 1
        elif (choice == 1) and (user_choice == 'r'):
            print('We both chose rock so it\'s a draw')
            ties_int = ties_int + 1

        if (choice == 2) and (user_choice == 'p'):
            print('We both chose paper so it\'s a draw')
            ties_int = ties_int + 1
        elif (choice == 2) and (user_choice == 's'):
            print('Me: paper, You: scissors. You win !')
            UserWin_int = UserWin_int + 1
        elif (choice == 2) and (user_choice == 'r'):
            print('Me: paper, You: rock. I win !')
            CompWin_int = CompWin_int + 1

        if (choice == 3) and (user_choice == 'p'):
            print('Me: scissors, You: paper. I win !')
            CompWin_int = CompWin_int + 1
        elif (choice == 3) and (user_choice == 's'):
            print('We both chose scissors so it\'s a draw')
            ties_int = ties_int + 1
        elif (choice == 3) and (user_choice == 'r'):
            print('Me: scissors, You: rock. You win !')
            UserWin_int = UserWin_int + 1

        count = count + 1

    print()
    print('### GAME OVER ###')
    print('You won: ',UserWin_int)
    print('I won: ',CompWin_int)
    print('There were ',ties_int,' draws')
    play_again = input('Play again? (y)es or (n)o? ')
print('Thanks for playing. Goodbye!')
