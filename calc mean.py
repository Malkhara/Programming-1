# Mohammd
# Python program to calculate the mean
# To be used in my stats class

import statistics

	
print("Welcom to Mohammd's program ..")
print()
print('This program will give you: mean \n')

numnersLimit = int(input('How many pairs? '))
alist = []
blist = []
for i in range(numnersLimit):
       count = numnersLimit
       if count != 0:
              user_input1 = float(input('Enter the first No. '))
              alist.append(user_input1)
              user_input2 = float(input('Enter the second NO. '))
              blist.append(user_input2)
              count =- 1
print('You enterd :',alist, blist)
print(" The mean is : ",statistics.mean(alist))
print(" The mean is : ",statistics.mean(blist))
print(" The mean of the two: ",(statistics.mean(alist)\
                                +statistics.mean(blist))/2)



