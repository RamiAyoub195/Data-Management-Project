# ECOR 1042 Deliverable 4 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Declan Foshaug"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101272097"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-130"

#==========================================#
# Place your script for your text_UI after this line

from load_data import *
from sort import *
from curve_fit import *
from histogram import *

def data_loader() -> list[dict]:
    """Returns a list of dictionaries for a file, the user will be prompted to enter a 
    file, an attribute and if necessary a level. 
    
    Please enter the name of the file: student-test.csv
    
    Please enter the attribute to use as a filter: All
    
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, {another element}]
    
    """
    global result
    possible_attributes = ['Health', 'Age', 'Failures']
    special_case = ['School']
    file = input('Please enter the name of the file: ')
    attribute = input('Please enter the attribute to use as a filter: ')
    combined = possible_attributes + special_case
    if attribute != 'All':
            if attribute in special_case:
                level = input('Please enter the level you wish to load: ')
                result = add_average(load_data(file, (attribute, level)))
                
            elif attribute in possible_attributes:
                level = int(input('Please enter the level you wish to load: '))
                result = add_average(load_data(file, (attribute, level)))
                
            else:
                while attribute not in combined:
                    print(f'Attribute not valid.\n Valid attributes are {combined} ')
                    attribute = input('Please enter the attribute to use as a filter: ')
                    
                if attribute in special_case:
                    level = input('Please enter the level you wish to load: ')
                    result = add_average(load_data(file, (attribute, level)))
                    
                elif attribute in possible_attributes:
                    level = int(input('Please enter the level you wish to load: '))
                    result = add_average(load_data(file, (attribute, level)))
    else:
        result = add_average(load_data(file, (attribute, -2)))
        
    return result       

def data_sorter() -> list[dict]:
    """Returns a list of dictionaries sorted. The user must first load the file in order 
    for the function to work. The user will be prompted to enter an attribute, order and if
    they would like to see sorted data or not.
    
    Precondition: User must load a file first !
    
    Please enter the attribute you want to use for sorting:
    'Age' 'StudyTime' 'Failures' 'G_Avg'
    : G_Avg
    
    Ascending (A) or Descending (D) order: D
    
    Data sorted. Do you want to display the data? (Y/N): Y
    
    [{'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14, 'G_Avg': 14.0}, {another element}]
    """
    
    outcome = ''
    possible_orders = ['A', 'D']
    possible_outcomes = ['Age', 'StudyTime', 'G_Avg', 'Failures']
    attribute = input("Please enter the attribute you want to use for sorting:\n'Age' 'StudyTime' 'Failures' 'G_Avg'\n:")
    if attribute in possible_outcomes:
        order = input('Ascending (A) or Descending (D) order: ')
        if order in possible_orders:
            display = input('Data sorted. Do you want to display the data? (Y/N): ')
            if display == 'Y':
                outcome = sort_by_key(loaded_data, order, attribute)            
        else:
            print('Invalid command.')
    
    else:
        while attribute not in possible_outcomes:
            attribute = input("Please enter the attribute you want to use for sorting:\n'Age' 'StudyTime' 'Failures' 'G_Avg'\n: ")
            
        if attribute in possible_outcomes:
            order = input('Ascending (A) or Descending (D) order: ')
            if order in possible_orders:
                    display = input('Data sorted. Do you want to display the data? (Y/N): ')
                    if display == 'Y':
                        outcome = sort_by_key(loaded_data, order, attribute)                     
            else:
                print('Invalid command.')
                
    return outcome

def data_best_fit() -> str:
    """Returns the line of best fit. The user must first load the file in order for the function to work.
    The user will be prompted to enter an attribute and polynomial.
    
    Precondition: attribute != 'School' and user must first load file
    
    Please enter the attribute you want to use to find the best fit for G_Avg:
    'Age', 'StudyTime', 'Failures', 'Health', 'Absences', 'G1', 'G2', 'G3
    : Age
    
    Please enter the order of the polynomial to be fitted: 3
    
    y = -0.36x^3+17.79x^2-295.06x^1+1635.84
    """
    value = ''
    possible_outcomes = ['Age', 'StudyTime', 'Failures', 'Health', 'Absemces', 'G1', 'G2', 'G3']
    attribute = input("Please enter the attribute you want to use to find the best fit for G_Avg:\n'Age', 'StudyTime', 'Failures', 'Health', 'Absences', 'G1', 'G2', 'G3\n: ")
    if attribute in possible_outcomes:
        polynomial = int(input("Please enter the order of the polynomial to be fitted: "))
        value = curve_fit(loaded_data, attribute, polynomial)        
    else:
        print('Invalid command.')

    return value

def data_histogram() -> None:
    """Returns a histogram data. The user must first load the file in order for the function to 
    work. The user will be prompted to enter an attribute:
    
    Precondition: User must load the file first!
    
    Please enter the attribute you want to use for plotting:
    'School', 'Age', 'StudyTime', 'Failures', 'Health', 'Absences', 'G1', 'G2', 'G3
    : Age
    
    <histogram is displayed>
    """
    expected = ''
    possible_attributes = ['School', 'Age', 'StudyTime', 'Failures', 'Health', 'Absences', 'G1', 'G2', 'G3']
    attribute = input("Please enter the attribute you want to use for plotting:\n'School', 'Age', 'StudyTime', 'Failures', 'Health', 'Absences', 'G1', 'G2', 'G3\n: ")
    if attribute in possible_attributes:
        expected = (histogram(loaded_data, attribute))
        
    else:
        print('Invalid command.')
    
    return expected
        
loaded_data = ''
command = ''
available_commands = """
The available commands are:
L)oad Data
S)ort Data
C)urve Fit
H)istogram
E)xit
"""

while command.upper() != 'E':
    
    print(available_commands)
    command = input('Please type your command: ')
    
    if command.upper() == 'L':
        print(data_loader())
        loaded_data = result
        
    elif command.upper() == 'S':
        if loaded_data == '':
            print('File not loaded. Please, load a file first.')
        else:   
            print(data_sorter())

    elif command.upper() == 'C':
        if loaded_data == '':
            print('File not loaded. Please, load a file first.')
        else:
            print(data_best_fit())
    
    elif command.upper() == 'H':
        if loaded_data == '':
            print('File not loaded. Please, load a file first.')
        else:
            print(data_histogram())

    else:
        if command.upper() != 'E':
            print('No such command.')
        
