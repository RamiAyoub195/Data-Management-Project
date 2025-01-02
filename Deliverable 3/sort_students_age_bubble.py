# ECOR 1042 Deliverable 3 - Individual submission for sort_students_age_bubble

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Rami Ayoub"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101261583"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-130"

#==========================================#
# Place your sort_students_age_bubble function after this line

def sort_students_age_bubble(age_dictionary: list[dict], ascend_descend_order: str) -> list[dict]:
    """Returns a list of dictionaries in ascending or decsending order specified by the user through 'A' or 'D' If and only if the list of
    dictionarys key contains 'Age'. If the key is not withing the dicionary list it returns a message to the
    user indicating the key is not present and returns the list as entered. 
    
>>> sort_students_age_bubble([{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}], "D") 
[{'Age': 19, 'School': 'MS'}, {'Age': 10, 'School': 'GP'}]

>>> sort_students_age_bubble([{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}], "A") 
[{'Age': 10, 'School': 'GP'}, {'Age': 19, 'School': 'MS'}]

>>> sort_students_age_bubble([{"School":"GP"}, {"School":"MS"}], "D") 
"Age" key is not present.
[{'School': 'GP'}, {'School': 'MS'}]
    """
    for x in age_dictionary:
        if 'Age' not in x: 
            print('"Age" key is not present.')
            return age_dictionary
    
    if ascend_descend_order.upper() == 'A':
        swap = True
        while swap:
            swap = False
            for i in range(len(age_dictionary) - 1): 
                if age_dictionary[i].get('Age', 0) > age_dictionary[i + 1].get('Age', 0): 
                    highest = age_dictionary[i]
                    age_dictionary[i] = age_dictionary[i + 1]
                    age_dictionary[i + 1] = highest
                    swap = True
        
    elif ascend_descend_order.upper() == 'D':
        swap = True
        while swap:
            swap = False
            for i in range(len(age_dictionary) - 1):
                if age_dictionary[i].get('Age', 0) < age_dictionary[i + 1].get('Age', 0):
                    highest = age_dictionary[i]
                    age_dictionary[i] = age_dictionary[i + 1]
                    age_dictionary[i + 1] = highest
                    swap = True 
                    
    return age_dictionary

# Do NOT include a main script in your submission
