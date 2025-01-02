# ECOR 1042 Deliverable 4 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Mazhar Kutukcu"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101277431"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-130"

#==========================================#
# Place your script for your batch_UI after this line

from load_data import *
from sort import *
from curve_fit import *
from histogram import *

def user_command(command):
    """Returns the users instructed commands per line in a file
    
    Precondition: User must enter a file!
    
    """
    global result
    possible_attributes = ['Health', 'Age', 'Failures']
    if command[0] == 'L':
        if command[2] == 'All':
            result = add_average(load_data(command[1], (command[2], -2)))
            print(add_average(load_data(command[1], (command[2], -2))))
        elif command[2] in possible_attributes:
            result = add_average(load_data(command[1], (command[2], int(command[3]))))
            print(add_average(load_data(command[1], (command[2], int(command[3])))))
        elif command[2] == 'School':
            result = add_average(load_data(command[1], (command[2], command[3])))
            print(add_average(load_data(command[1], (command[2], command[3]))))
        
    elif command[0] == 'S':
        if command[3] == 'Y':
            print(sort_by_key(result, command[1], command[2]))
        else:
            print('Data sorted.')
        
    elif command[0] == 'C':
        print(curve_fit(result, command[1]), int(command[2]))
        
    elif command[0] == 'H':
        print(histogram(result, command[1]))
        
    return None

file_name = input("Please enter the name of the file where your commands are stored: ")

file = open(file_name, 'r')

read_lines_of_file = file.readlines()

for i in read_lines_of_file:
    command = i.strip().split(';')
    user_command(command)
    
    


        
    
    
        
        
    

