##########################################             
# Mohammd-AlKharaan-project05
#
# CPS 201 Project #05
# Mohammd AlKharaan
#
# Tip Calculator Program
#
# ======= Algorithm =======                            
# 1- Enter the bill amount                             
# 2- Enter the Tip percentage (1 - 100)                
# 3- print the total bill with the tip                 
# 4- check if the user want to split the bill          
# 5- if yes, prompt the user to enter how many people  
# 6- Divide the bill on the people number              
# 7- Print Goodbye! and stop                                                                              
##########################################

try:
    def calcTip(bill, percentage):
        ''' Function: calcTip(bill, percentage)
            bill amount and tip percentage
            Returns: float bill amount, and float tip percentage
            Algorithm:
                 recieve the input tip from the user
                 devide the tip by 100
                 mulitply the number by the bill
                 round the number (float)
                 return the rounded tip number (float)
        '''
        tip = float(bill * (percentage / 100)) # calculate the tip
        tip_round = round(tip, 2) # round the tip
        return tip_round # return the rounded tip value
    
    def calcTotal(bill, tip):
        ''' Function: calcTotal(bill, tip)
            bill is representing the bill before the tip
            tip represenintg the amout of the tip
            return the sum of the bill and tip as a float number
            Algorithm:
                 recieve the bill and tip
                 devide the tip by 100
                 multiply the tip by the bill
                 add the result to the bill
                 round the number (float)
                 return the rounded total amount (float)          
        '''
        tip_value = float(bill * ( tip / 100)) # calculate the total
        total_float = float(bill + tip_value) 
        total_float_round = round(total_float, 2) # round the total
        return total_float_round # return the rounded total

    def splitChecker(total, people):
        ''' Function: splitChecker(total, people)
            total is the amount of the bill with the tip
            poeple is the number you want to divide the bill on
            returns how many dollars everyone is paying
            Algorithm:
                  receivee the total and the number of poeple
                  devide the total by the number of people
                  round the number (float)
                  return the rounded total of each person (float)
        '''
        ind_total = float(total / people) # calculate indivual paying
        ind_total_round = round(ind_total, 2) # rouund the indivual total
        return ind_total_round # return the rounded indivual total
            
    # the main program
    print('Tip Calculator Program')
    print('Author: Mohammd AlKharaan')
    bill_input = float(input('Bill amount? ')) # prompt for the bill amount
    tip_input = float(input('Tip percentage (1-100%)? ')) # desired tip percentage
    if (tip_input > 0) and (tip_input <= 100): # to make the tip inside the range
        bill_tip = calcTip(bill_input, tip_input) # assign these inputs to the calcTip function
        bill_total = calcTotal(bill_input, tip_input) # assign theese inputs to the calcTotal function
        print('Tip is ${:>.2f}'.format(bill_tip)) # print the results
        print('Your total bill is ${:>.2f}'.format(bill_total))
        split = (input('Split the check? (Y/N) ')) # prompt for indivual paying
    else:
        pass # end the loop
    if (split == 'Y' or split =='y'):
        people_sum = int(input('How many people? ')) # number of indivuals
        ind_total = (splitChecker(bill_total, people_sum)) # assign these inputs to splitChecker function
        print('Each person owes ${:>.2f}'.format(ind_total)) # print the results
              
    else:
        pass # end the loop
    

                
                
except:
    print('Error: invalid numeric input')
print('\nGoodbye!') # Stop
