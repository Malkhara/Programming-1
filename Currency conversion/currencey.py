###############################################################################           
# Mohammd-AlKharaan-Assignment04
#
# CPS 202 Assignment #04
# Mohammd AlKharaan
#
# Larger Program
#
##########################################


'''


Author : Mohammd AlKharaan 202 Assignment 04
Currencey class to convert currencies and handle arithmetic operations.

'''

class Currency(object):
       ''' Currency class '''
       
       # # # Required methods # # #
       def __init__(self, amount=0, currencyCode='USD'):
              ''''
              Class method: __init__(self, amount=0, currencyCode='USD')
              takes self, amount and Currency code as arguements
              Returns nothing.
              '''
              if type(amount) is str:
                     self.__amount = 0
              if type(currencyCode) is not str:
                     self.__currencyCode = 'USD'
              else:
                     self.__amount = amount
                     self.__currencyCode = currencyCode

       def __str__(self):
              ''''
              Class method:__str__(self)
              takes self as argument
              Returns amount and currency code as string
              ''' 
              return "{}: {}".format(self.__amount, self.__currencyCode)

       def __repr__(self):
              ''''
              Class method:__repr__(self)
              takes self as argument
              Returns the str method
              ''' 
              return self.__str__()

       def convert_to(self, convCurrencyCode):
              ''''
              Class method:convert_to(self, convCurrencyCode)
              takes self, and Currency code as arguements
              Converts the amount to the cuurency code given
              Returns float of amount converted.
              '''
              self.__convCurrencyCode = convCurrencyCode
              import urllib.request
              web_obj = urllib.request.urlopen('https://www.google.com/\
finance/converter?a={}&from={}&to={}'.format(self.__amount,self.__currencyCode\
                                             ,self.__convCurrencyCode))
              web_obj_str = str(web_obj.read())
              web_obj.close()
              result_line_start = web_obj_str.find('<span class=bld>')
              result_line_end =web_obj_str.find('</span>')
              result = web_obj_str[(result_line_start+16):(result_line_end-3)]
              self.__last_result = float(result)
              return self.__last_result, self.__convCurrencyCode
                                   
                                   
       
              


       def __add__(self, param):
              ''''
              Class method:__add__(self, param)
              takes self and paramas argument
                         if param is from Currency class
                         it will convert it to self currency
                         then will do the math.

                         if param not from Currency class
                         it will do the math without converting
                         
              Returns the result of the addition
              ''' 
              if isinstance(param, Currency):
                     if self.__currencyCode != param.__currencyCode:
                            newCurr = param.convert_to(self.__currencyCode)
                            result = self.__amount + newCurr[0]
                            return '{} {}'.format(result, self.__currencyCode)
                     elif self.__currencyCode == param.__currencyCode:
                            result = self.__amount + param.__amount
                            return '{} {}'.format(result, self.__currencyCode)
              else:
                     the_sum = self.__amount + param
                     return the_sum


       def __radd__(self, param):
              ''''
              Class method:__radd__(self, param)
              takes self and paramas argument
                         
              Returns the result of the addition
              ''' 
              the_sum = param + self.__amount
              return the_sum


       def __sub__(self, param):
              ''''
              Class method:__sub__(self, param)
              takes self and paramas argument
                         if param is from Currency class
                         it will convert it to self currency
                         then will do the math.

                         if param not from Currency class
                         it will do the math without converting
                         
              Returns the result of the subtraction
              ''' 
              if isinstance(param, Currency):
                     if self.__currencyCode != param.__currencyCode:
                            newCurr = param.convert_to(self.__currencyCode)
                            result = self.__amount - newCurr[0]
                            return '{} {}'.format(result, self.__currencyCode)
                     elif self.__currencyCode == param.__currencyCode:
                            result = self.__amount - param
                            return '{} {}'.format(result, self.__currencyCode)
              else:
                     result = self.__amount - param
                     return result


       def __rsub__(self, param):
              ''''
              Class method:__rsub__(self, param)
              takes self and paramas argument
                         if param is from Currency class
                         it will convert it to self currency
                         then will do the math.

                         if param not from Currency class
                         it will do the math without converting
                         
              Returns the result of the reversed subtraction
              '''
              if isinstance(param, Currency):
                     if self.__currencyCode != param.__currencyCode:
                            newCurr = param.convert_to(self.__currencyCode)
                            result = newCurr[0] - self.__amount
                     return '{} {}'.format(result, self.__currencyCode)
              else:
                     result = param - self.__amount
                     return result


       def __gt__(self, param):
              ''''
              Class method:__gt__(self, param)
              takes self and paramas argument
                     Compare the amount of self with param
                         
              Returns True or False
              '''
              if isinstance(param, Currency):
                     if self.__currencyCode != param.__currencyCode:
                            newCurr = param.convert_to(self.__currencyCode)
                            return self.__amount > newCurr[0]
                     if self.__amount == param:
                            return 'Equal'
                     else:
                            return self.__amount > param



