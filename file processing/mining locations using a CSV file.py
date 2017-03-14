####################################################################
# alkharaan-zimmer-proj06
#
# CPS 201 project #06
# Mohammd Alkharaaan - Jeffrey Zimmer
#
# designed to create a list of acceptable mining locations using a
#     CSV list to solve project #06.
#
# algorithm:
#   1.create function for removing extraenous information, converts
#       elements into required types, returns tuple.
#   2.create function that returns list of tuples utilizing the 1st
#       function, will also reprompt if given invalid filename.
#   3.create function to remove unwanted mining locations and return
#       a completely new list.
#   4.create function to write this new list to craters.txt file.
#   create main program:
#   request input for filename, reprompt if invalid filename.
#   call for 2nd function to create list
#   call for 3rd function to update list with acceptable locations
#   call for 4th function to write to output file
####################################################################

def get_crater_tuple(line_str):
    
    '''has a string as a parameter and returns a tuple of the
       form (ID , name , latitude , longitude , diameter)

       Algorithm:
           create an empty list
           convert each element into the required type
           append the list with the different types
           return tuple
    '''

    converted_list = []
    
    line_str.strip()

    # split string on comma to create a list
    
    line_list = line_str.split(',')
    
    # convert into desired type and append list
    
    converted_list.append(int(line_list[0]))
    converted_list.append(str(line_list[1]))
    converted_list.append(float(line_list[2]))
    converted_list.append(float(line_list[3]))
    converted_list.append(float(line_list[4]))

    return tuple(converted_list)

def read_craters(filename):
    
    '''Accepts a filename, which is a string, and returns list
       of crater tuples as read from the file

       Algorithm:           
           open filename file in read 'mode'
           create an empty list to append tuples to
           create a loop to reprompt if invalid filename
           call the get_crater_tuple function
           append list with tuples
           return tuple list
           close filename file
    '''
    
    valid_input = False   # control variable for while-try-except
    
    # begin while loop, try-except block
    
    while valid_input == False: 
        
        try:
            open_file = open(filename, 'r')
            valid_input == True         # update control variable             
            return_list = []
            line_count = 3      # line counter to skip header
            
            # begin for loop to skip header and append return_list
            
            for line in open_file:
                line_count -= 1
                if line_count == 0:
                    pass 
                    for line in open_file:
                        return_list.append(get_crater_tuple(line))
                        
            open_file.close()
            
            # end for loop to skip header and append return_list
            
            return return_list

        except IOError:
            print('Invalid filename')
            filename = input("Name of file with crater data: ")
            
    # end while loop, try-except block
    
def get_eligible_craters(crater_list):
    
    '''outputs a new list by iterating through a given list and
       removes entries that do not meet lat., long., and diameter
       requirements.

       algorithm:
           create an empty new list
           iterate through crater_list using a boolean construct
               to determine eligibility to be added to new list
           append new list with eligible mining sites
    '''

    acceptable_list = []

    # begin for loop, performs boolean condition to verify mining
    
    for i in crater_list:
        if (i[2] >= -40) and (i[2] <= 50):            
            if (i[3] >= 40) and (i[3] <= 135):
                if i[4] > 60:
                    acceptable_list.append(i)
                    
    # end for loop
    
    return acceptable_list    

def write_craters(eligible_crater_list):
    
    '''takes an eligible list of crater tuples and write them to a
       file named craters.txt, returns nothing

       algorithm:
           open an ouput file called craters.txt
           write and format a header file for output file
           iterate through the list of tuples to write to file
           write and format the result into the file
           close the file
    '''
    
    output_file = open('craters.txt', 'w')

    # print file header to output file
    
    print('{}{:>8}{:>17}{:>13}{:>16}'.format('CRATER ID','NAME',\
          'LATITUDE','LONGITUDE','DIAMETER (km)')\
          ,file = output_file)

    # begin for loop
    
    for element in eligible_crater_list:

        # would not print out correctly without the 4 spaces in
        #    between the first 2 elements. element 2 would just
        #    'stick' to element 1 no matter what the value given
        
        print('{:9}    {:<13}{:>8.2f}{:>13.2f}{:>16.1f}'.format\
              (element[0], element[1], element[2], element[3],\
               element[4]),file=output_file)

    # end for loop
        
    output_file.close()

############ Main Program #############
    
filename = input("Name of file with crater data: ")
crater_list = read_craters(filename)
eligible_crater_list = get_eligible_craters(crater_list)
write_craters(eligible_crater_list)

