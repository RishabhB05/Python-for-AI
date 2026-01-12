#  Module: single file containing Python code which can be imported in other files
#packeges : folder containing multiple modules
#libraries : collection of packages and modules


from math import sqrt, pi
print("Square root of 16 is:", sqrt(16))
print("Value of pi is:", pi)


import random 
random_number = random.randint(1, 100)
choice = random.choice(['apple', 'banana', 'cherry'])
print("Random number:", random_number)
print("Random choice:", choice)


import datetime
now = datetime.datetime.now()
print("Current date and time:", now)

import os
current_directory = os.getcwd()
print("Current working directory:", current_directory)

import pandas as pd
