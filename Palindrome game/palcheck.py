###############################################################################
# Mohammd AlKharaan
# CPS-311 project-04
#

from arraystack import *
from linkedstack import *

def inputToStack(userPrompt,userType):
    ''' takes user prompt and stack type
        returns a stack with the specified type by the user
    '''
    userPrompt = userPrompt.lower().replace(" ", "")
    # no spaces and all lower case
    if userType == 'Array' or userType == 'array':
            return ArrayStack(userPrompt)
    # end if
    elif userType == 'linked' or userType == 'Linked':
        # if the user picked linked stack
        return LinkedStack(userPrompt)
    # end elif
    else: # if it is not array or linked return false
        return False


def checkPalindrome(userStack):
    ''' takes the stack and checks to see if it is palindrome
        returns boolean.
        taking advantage of the fact that the stacks' for-loops
        look at the stack from the bottom-up, but the peek() method
        looks at the stack from the top-down
    '''
    tempStack = type(userStack)(userStack)
    # create a temp stack with the type of the user stack
    for i in userStack:
        # loop through the user stack
        if tempStack.peek() == i:
            # if the first item in temp stack is i
            tempStack.pop()
            # remove it from the stack
    # end for loop
    return tempStack.isEmpty()


#### Main program ####
def main():
    validInput = True
    while validInput:
        try:
            userPrompt = str(input('Enter a string: '))
            # prompt for input to check it
            userType = str(input('Type of stack: '))
            # prompt for the type as well
            convertToStack = inputToStack(userPrompt, userType)
            # call the func to convert the str to stack object
            if convertToStack: # if not false
                isPalindrome = checkPalindrome(convertToStack)
                # calling checkPalindrome func
                if isPalindrome:
                    print('YES! "',userPrompt,'" Is a palindrome.')
                else:
                    print('NO! "',userPrompt,'" Is NOT a palindrome.')
                print()
                againPrompt = str(input('Again? (y or n) '))
                # re-prompt the user for more trials
                if againPrompt == 'y':
                    continue
                # if user wants to play again, go back to top of loop
                else:
                    validInput = False
                    print()
                    print('Thanks for playing!')
                # if user wants to stop, 
                # valid input is false to breake the while loop
                # and print thanks for playing
            # end if convertToStack:
            else:
                # if user typed something beside linked or array
                # print this msg, and continue the program from the top
                print ('choose (array or linked) ')
                continue

        except: # to exit the program gracefully!
            print('Something went wrong!')
            print('Restart the program')


if __name__ == "__main__":
    main()

