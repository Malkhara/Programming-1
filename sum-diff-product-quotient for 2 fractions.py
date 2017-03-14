###############################################################################           
# Mohammd-AlKharaan-Assignment02
#
# CPS 202 Assignment #02
# Mohammd AlKharaan
#
# Quick Program
#
# ======= Algorithm =======                            
# 1- Prompt the user for 2 fractions
# 2- create function to do the math
# 3- display sum, diffrence, product, and quotient
##########################################

def sum_of_fractions(first_fraction, second_fraction):
        ''' Function: sum_of_fractions(first_fraction, second_fraction)
            takes the tow fractions as tuples
            Returns: sum of fraction also as a tuple
            Algorithm:
                 recieve the input fractions
                 add fractions together
                 return the sum of the fractions as a tuple
        '''
        if first_fraction[1] == second_fraction[1]:
                sum_fractions = ((first_fraction[0]+second_fraction[0])\
                                 ,first_fraction[1])
                return sum_fractions
        else:
                arth_fraction = (first_fraction[0]*second_fraction[1], \
                                 first_fraction[1]*second_fraction[1])
                arth_fraction1 = (second_fraction[0]*first_fraction[1], \
                                  second_fraction[1]*first_fraction[1])
                arth_fraction2 = ((first_fraction[0]*second_fraction[1]\
                                   +second_fraction[0]*first_fraction[1]),\
                                  first_fraction[1]*second_fraction[1])
                return arth_fraction2

def dif_of_fractions(first_fraction, second_fraction):
        ''' Function: dif_of_fractions(first_fraction, second_fraction)
            takes the tow fractions as tuples
            Returns: diffrence of fraction also as a tuple
            Algorithm:
                 recieve the input fractions
                 subtract fractions together
                 return the diffrence of the fractions as a tuple
        '''
        if first_fraction[1] == second_fraction[1]:
                sum_fractions = ((first_fraction[0]-second_fraction[0]),\
                                 first_fraction[1])
                return sum_fractions
        else:
                arth_fraction = (first_fraction[0]*second_fraction[1], \
                                 first_fraction[1]*second_fraction[1])
                arth_fraction1 = (second_fraction[0]*first_fraction[1], \
                                  second_fraction[1]*first_fraction[1])
                diffrence = ((arth_fraction[0] - arth_fraction1[0],\
                              second_fraction[1]*first_fraction[1]))
                return diffrence

def mult_of_fractions(first_fraction, second_fraction):
        ''' Function: mult_of_fractions(first_fraction, second_fraction)
            takes the tow fractions as tuples
            Returns: product of fraction also as a tuple
            Algorithm:
                 recieve the input fractions
                 multiply the  fractions
                 return the product of the fractions as a tuple
        '''
        product = ( (first_fraction[0]*second_fraction[0]), \
                    (first_fraction[1]*second_fraction[1]) )
        return product

def div_of_fractions(first_fraction, second_fraction):
        ''' Function: div_of_fractions(first_fraction, second_fraction)
            takes the tow fractions as tuples
            Returns: quotient of fraction also as a tuple
            Algorithm:
                 recieve the input fractions
                 divide the  fractions
                 return the quotient of the fractions as a tuple
        '''
        arth_fraction = first_fraction[0] * second_fraction[1]
        arth_fraction1 = first_fraction[1] * second_fraction[0]
        quotient = (arth_fraction, arth_fraction1)
        return quotient

def main():
        try:
                # Prompt the user for numbers
                first_numerator = int(input('Enter the first \
numerator: '))
                first_denominator = int(input('Enter the first\
 denominator: '))
                while first_denominator == 0:
                        # accept non-zero value only
                        first_denominator = int(input('Enter non-zero\
 denominator: '))
                        # End while loop

                second_numerator = int(input('Enter the second \
 numerator: '))
                second_denominator = int(input('Enter the second \
 denominator: '))
                while second_denominator == 0:
                        # accept non-zero value only
                        second_denominator = int(input('Enter non-zero\
 denominator: '))
                        # End while loop
                #invoke functions
                first_fraction_tuple = (first_numerator,\
                                        first_denominator)
                second_fraction_tuple = (second_numerator,\
                                         second_denominator)
                sum_fraction = sum_of_fractions(first_fraction_tuple\
                                        , second_fraction_tuple)
                dif_fraction = dif_of_fractions(first_fraction_tuple\
                                        , second_fraction_tuple)
                mult_fraction = mult_of_fractions(first_fraction_tuple\
                                        , second_fraction_tuple)
                div_fraction = div_of_fractions(first_fraction_tuple\
                                                , second_fraction_tuple)
                # Display the results
                print('\n \n(numerator, denominator)')
                # to make it more user-friendly
                print(' Sum:        ',sum_fraction)
                print(' Diffrence:  ',dif_fraction)
                print(' Product:    ', mult_fraction)
                print(' Quotient:   ', div_fraction)
        except ValueError: # Handling the ValueError gracefully
              print('This program accepts only integers.\nThank you !')
              # End try-except loop


main()
