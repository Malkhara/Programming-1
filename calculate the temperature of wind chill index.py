###################################################################################
# Mohammd-Alkharaan-project02.py                                                  #
#                                                                                 #
# CPS 201 project #02                                                             #
# Mohammd Alkharaan                                                               #
#                                                                                 #
# This program is designed to calculate the temperature of wind chill index       #
#                                                                                 #
# Algorithm                                                                       #
# Prompt the user to enter an air tempreature measurement in degrees Fahrenheit   #
# Prompt the user to enter a wind speed measurement in miles per hour             #
# Perform the math specified in the NWS WCT                                       #
# Perform a series of artithmetic operations                                      #
# Display the results                                                             #
###################################################################################

import math

# Identifying the variables
air_temperature = input(' Enter the Air Temperature Measurement (degrees F):')
air_temperature_flo = float(air_temperature)
# Air tempreature measurement in degrees Fahrenheit, as float

wind_speed = input('Enter the Wind Speed Measurement (MPH) :')
wind_speed_flo = float(wind_speed)
# Wind speed measurement in miles per hour, as float 

# Performing the equation to get the wind chill
wind_chill = (35.74 + (0.6215 * air_temperature_flo) - (35.75 * (wind_speed_flo ** 0.16)) + ( (0.4275 * air_temperature_flo) * (wind_speed_flo ** 0.16)))

# Displsying the results
print(' For a temperature of', air_temperature_flo, \
      ' degrees F \n and wind speed of', wind_speed_flo, \
      'MPH \n The wind Chill Temperature index is : ', round(wind_chill, 3))
