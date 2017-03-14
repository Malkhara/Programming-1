###############################################################################           
# Mohammd-AlKharaan-Assignment03
#
# CPS 202 Assignment #03
# Mohammd AlKharaan
#
# Meduim Program
#
# You have to have *.txt file so the program runs on it
##########################################

def open_read_file(user_input):
        ''' Function: open_read_file(user_input)
            takes the user input as arguement
            Returns: the file in a list
            Algorithm:
                 recieve the input file
                 read it
                 return it
        '''
        file = open(user_input, 'r') # open the file
        new_list = [] # creat a new list
        for line in file:
                if ',' in line:
                        for word in line.split(','):
                                new_list.append(word)
                else:
                        for word in line.split():
                                new_list.append(word)
        # loop to append the words to the list
        # end loop
        return new_list

def add_to_dict(str_list):
        ''' Function: add_to_dict(str_list)
            takes the string list as arguement
            Returns: a Dictionary
            Algorithm:
                 recieve the string listt
                 loop through it
                 sort data and make them in lower case
                 return dict
        '''
        new_dict = {} # creat a new dictionary
        for values in str_list:
                new_dict[values] = (sorted(values.lower()))
                # sort strings and make them into lower case
                # end the loop
        return new_dict

def check_anagrams(my_dict):
        ''' Function: check_anagrams(my_dict)
            takes the dictionary as arguement
            Returns: a anagrams dict
            Algorithm:
                 recieve the dictionary
                 loop through it
                 check for anagrams
                 return anagrams dict
        '''
        anag_dict = {}# creat a new dictionary
        for key in my_dict:
                for ele in my_dict:
                        if key is not ele:
                                if my_dict[key] == my_dict[ele]:
                                      anag_dict[ele] =   my_dict[key]
        # loop to check for anagrams and add them to dict
        # end loop
        return anag_dict

##def print_dict(anag_dict):
##        new_list = []
##        print_list = []
##        for key in anag_dict:
##                new_list.append(key)
##        for ele in new_list:
##                for let in ele:
##                    print_list.append(ele)    
##        return print_dict
        
                        

def main():
        try:
                user_input = input('What is the file name ? ')
                # prompt user for file name
                read_file = (open_read_file(user_input))
                # invoke function to read the file
                add_to_dic = (add_to_dict(read_file))
                # invoke function to add to dict
                anag_dict = check_anagrams(add_to_dic)
                # invoke function to have the anagrams dict
                if len(anag_dict) == 0:
                        print('No Anagrams found in this file')
                else:
                        print('Anagrams found in file: ')
                        for key in anag_dict:
                                print(key)
                #print(sorted(print_dict(anag_dict)))
                # end loop
                
        except FileNotFoundError: # to deal with that gracefully
                print('File not found')







main()
