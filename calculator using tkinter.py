###############################################################################           
# Mohammd-AlKharaan-Assignment06
#
# CPS 202 Assignment #06
# Mohammd AlKharaan
#
#  Program
#
# How to save something to memory!
# How to do OFF, ON !
# how to make the x^y work !
##########################################


from tkinter import *
from math import sqrt, pow
class Calculator:

       def __init__ (self):

              window = Tk()
              window.title('Calculator')

              self.string = StringVar()
              entry = Entry(window,textvariable=self.string, bg='white')
              entry.grid(row=0,column=0,columnspan=6)
              entry.focus()

              ButtonList = ['CE', 'C', 'OFF', 'ON',
                      'MC', 'M+', 'M-', 'MR',
                      '\u221a', 'x\u00b2', 'x^y', '+',
                      '7', '8', '9', '-',
                      '4', '5', '6', '*',
                      '1', '2', '3', '/',
                      '0', '.', '+-', '=']

              rowNum = 2 
              colNum = 1

              self.memory = 0
               
              for string in ButtonList:
                   
                   if colNum < 4:
                       Button(window, text = string, height = 2, width = 3,
                              command = lambda string = self.string,q=string:
                              self.processButton(q)).grid(row = rowNum, column = colNum)
                       colNum = colNum + 1
                   elif colNum == 4:
                       Button(window, text = string, height = 2, width = 3,
                              command = lambda  string = self.string, q=string:
                              self.processButton(q)).grid(row = rowNum, column = colNum)
                       rowNum = rowNum + 1
                       colNum = colNum - 3  
              window.mainloop()

       def processButton(self, x):
              
              self.string.set(self.string.get()+x)
              
              if x=='CE':
                     operatorsList = ['+','-','*','/']
                     for i in operatorsList:
                            if i in self.string.get()[0:-1]:
                                   self.string.set(self.string.get()[0:self.string.get().find(i)+1])
                            else:
                                   self.string.get()[0:-1]
                   
              if x=='C':
                    self.string.set('') 
              if x=='OFF':
                     self.string.set('')
              if x=='ON':
                     if (self.string.get()[0:-2]) =='':
                            self.string.set(0) 
                     elif (self.string.get()[0:-2]) ==0:
                            
                            self.string.set(0)
                     else:
                            self.string.set(self.string.get()[0:-2])
                    
              if x =='MC':
                     self.string.set(self.string.get()[0:-2])
                     self.memory = 0
              if x =='M+':
                     addMem = float(self.string.get()[0:-2])
                     self.memory = self.memory + addMem
                     self.string.set(self.memory)
                     
              if x =='M-':
                     subMem = float(self.string.get()[0:-2])
                     self.memory = self.memory - subMem
                     self.string.set(self.memory)
              if x =='MR':
                     self.string.set(self.memory)
              if x =='=':
                     if '^' in self.string.get()[0:-1]:
                            self.string.get()[0:-1].find('^')
                            result = float(self.string.get()[0:self.string.get()[0:-1].find('^')]) ** float(self.string.get()[self.string.get()[0:-1].find('^')+1:-1])
                            self.string.set(result)
                     else:
                            self.string.set(eval(self.string.get()[0:-1]))
              if x =='\u221a':
                     self.string.set(sqrt(float(self.string.get()[0:-1])))
              if x =="x\u00b2":
                     self.string.set(pow(float(self.string.get()[0:-2]),2))
              if x =="x^y": 
                     (self.string.set('{}^'.format((self.string.get()[0:-3]))))
              if x =='+-':
                     if self.string.get()[0].isdigit():
                            self.string.set('-{}'.format(self.string.get()[0:-2]))
                     else:
                           self.string.set('{}'.format(self.string.get()[1:-2])) 

Calculator()
