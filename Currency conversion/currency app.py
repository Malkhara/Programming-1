###############################################################################           
# Mohammd-AlKharaan-Assignment04
#
# CPS 202 Assignment #04
# Mohammd AlKharaan
#
# Larger Program
#
# ### Criteria not met: ###
# loop to deduct from the amount ( Instead I prompt for amount every time)
# as a result, I couldn't use overdrawn when account is 0 or minus
# When subtracting USD from amount it does'n work
##########################################

from Currency import *


def display_message():
       '''
       Function display_message()
       to display the message for the application
       '''

       print('This applications asks for account amount\
\nand deal with deductions from another currencies\n')




def user_amount():
       '''
       Function user_amount():
       takes no arguemetn
       splits the user input
       return float and str
       '''

       user_input = input('Enter expense deduction XXX YYY\n(X is a number, Y is currency code) : ')
       user_input_split = user_input.split() # to split the string
       float_value = float(user_input_split[0]) # slice to have float
       str_value = str(user_input_split[1]) # slice for str
       return float_value, str_value

def sub_currencies(curr1, curr2):
       '''
       Function sub_currencies(curr1, curr2)
       takes 2 currencies as arguement
       performs the subtraction method from Currency class
       return the result
       '''

       sub_currencies = curr1 - curr2
       return sub_currencies


#### Main program ####
def main():

       display_message()
       while True:
              try:
                     
                     account = float(input('Enter your amount: '))
                     invoke_class_account = Currency(account)
                     invoke_class_account = Currency(account)
                     user_input = user_amount()
                     invoke_class_user_input = Currency(user_input[0], user_input[1])
                     total = sub_currencies(invoke_class_account,invoke_class_user_input)
                     print(total)
              except:
                     print(' Enter values correctly')
                     continue



main()
