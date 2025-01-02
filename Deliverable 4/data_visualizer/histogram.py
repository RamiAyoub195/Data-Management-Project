# ECOR 1042 Deliverable 4 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Adam Rickert"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101285295"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-130"

#==========================================#
# Place your histogram function after this line

import matplotlib.pyplot as plt
import numpy as np
from load_data import *

def histogram(list_of_dictionaries: list[dict], attribute: str) -> None:
    """The function returns a historgram for a selected attribute
    
    Precondition: None
    
>>> histogram(add_average(load_data('student-test.csv', ('All', -2))), 'Age')
<displays histogram>

>>> histogram(add_average(load_data('student-test.csv', ('All', -2))), 'Health')
<displays histogram>

>>> histogram(add_average(load_data('student-test.csv', ('All', -2))), 'Health')
<displays histogram>
    """
    dictionary = {}
    sorted_dictionary_keys = []
    sorted_dictionary = {}
    x_values = []
    y_values = []
    interval = 1
    
    for i in list_of_dictionaries:
        value = i[attribute]
        if isinstance(value, float) == True:
            value = round(value/interval) * interval 
        else:
            value = value
        
        if value not in dictionary:
            dictionary[value] = 1
        else:
            dictionary[value] += 1
        
    for i in dictionary.keys():
        sorted_dictionary_keys.append(i)
        
    swap = True
    while swap:
        swap = False
        for i in range(len(sorted_dictionary_keys) -1):
                if sorted_dictionary_keys[i] > sorted_dictionary_keys[i+1]:
                    aux = sorted_dictionary_keys[i]
                    sorted_dictionary_keys[i] = sorted_dictionary_keys[i+1]
                    sorted_dictionary_keys[i+1] = aux
                    swap = True 
                    
    for i in sorted_dictionary_keys:
        sorted_dictionary[i] = dictionary[i]
        
    for k, v in sorted_dictionary.items():
        x_values.append(k)
        y_values.append(v)

    fig_1 = plt.figure()
    plt.title(f"Number of Students for each {attribute} Level")
    plt.xlabel(f"{attribute} Levels")
    plt.ylabel("Number of Students")
    plt.bar(x_values, y_values, color='red')
    plt.show()  
    
    return None