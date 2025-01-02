# ECOR 1042 Deliverable 4 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Rami Ayoub"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101261583"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-130"

#==========================================#
# Place your curve_fit function after this line

import matplotlib.pyplot as plt
import numpy as np
from load_data import *

def curve_fit(list_of_dictionaries: list[dict], key_attribute: str, poly_degree: int) -> str:
    """Returns a string that represents the equation of the best fit line for the average of the G_Avg 
    for a specific attribute levels chosen.
    
    Precondition: key_attribute != 'School'
    
>>> curve_fit(add_average(load_data('student-test.csv', ('All', -2))), 'Health', 3)
'y = -1.16x^3+10.65x^2-28.23x^1+28.08'

>>> curve_fit(add_average(load_data('student-test.csv', ('All', -2))), 'StudyTime', 2)
'y = -0.43x^2+2.37x^1+6.04'

>>>curve_fit(add_average(load_data('student-test.csv', ('All', -2))), 'Failures', 6)
'y = 2.72x^3-12.15x^2+11.76x^1+9.0'
    """
    dictionary = {} #creates an empty dictionary
    sorted_dictionary = {} #creates an empty dictionary
    sorted_dictionary_keys = [] #creates an empty list
    x_values = [] #creates an empty list 
    y_values = [] #creates an empty list
    
    for i in list_of_dictionaries: #iterates through the list of dictionaries
        if i[key_attribute] not in dictionary: #if the value of the attribute is not in dictionary
            dictionary[i[key_attribute]] = [] #creates a key as attribute level with a value of an empty list 
        dictionary[i[key_attribute]].append(i.get('G_Avg')) #appends the value of every g_average for that attribute key level
        
    for i in dictionary.keys(): #Puts dictionary keys in a list
        sorted_dictionary_keys.append(i)
        
    swap = True
    while swap: #Sorts list of keys
        swap = False
        for i in range(len(sorted_dictionary_keys) -1):
                if sorted_dictionary_keys[i] > sorted_dictionary_keys[i+1]:
                    aux = sorted_dictionary_keys[i]
                    sorted_dictionary_keys[i] = sorted_dictionary_keys[i+1]
                    sorted_dictionary_keys[i+1] = aux
                    swap = True 
                    
    for i in sorted_dictionary_keys: #Sorts the dictionary and puts it 
        sorted_dictionary[i] = dictionary[i]
    
    for k, v in sorted_dictionary.items(): #Adds the keys to the x_values list and average of G_Avg to the y_values list
        x_values.append(k)
        y_values.append(round(sum(v)/len(v), 2))
    
    if poly_degree > len(sorted_dictionary): #To follow the formula N-1 data set points if it exceeds the length of the data points
        poly_degree = len(sorted_dictionary) - 1
    else:
        poly_degree = poly_degree      

    z = np.polyfit(x_values, y_values, poly_degree) 
    
    if z[0] >= 0:
        function = 'y = '
    else:
        function = 'y = -'
        
    for i in range(poly_degree + 1): #Creates the string function from the z polyfit funcion
        if len(z) > (i + 1):
            if z[i + 1] >= 0:
                polynomial = str(round(abs(z[i]), 2)) + 'x^' + str(poly_degree) +  '+'
                poly_degree -= 1
            else:
                polynomial = str(round(abs(z[i]), 2)) + 'x^' + str(poly_degree) +  '-'
                poly_degree -= 1
        else:
            polynomial = str(round(z[i], 2))
            
        function += polynomial
    
    return function 
    
# Do NOT include a main script in your submission
