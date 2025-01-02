# ECOR 1042 Deliverable 1 - Individual submission for student_school_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Rami Ayoub"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101261583"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-130"

#==========================================#
# Place your student_school_list function after this line

def student_school_list(file_name: str, school_name: str) -> list[dict]:
    """Returns a list of dictionaries for several students, the dictionary includes
    student age, studytime, failure, health, absences, G1 (first period grade), G2(second
    period grade) and G(final grade) for a chosen school. If a school is not found in the
    data, an empty list is returned.
    
    Precondition: None
    
>>> student_school_list('student-mat.csv', 'GP')
    [{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}]
    
>>> student_school_list('student-mat.csv', 'MB')
    [{'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {another element}]
    
>>> student_school_list('student-mat.csv', 'CU')
    []
    """
    infile = open(file_name, 'r') # Opens the file and reads from the file 
    next(infile) # Travreses to the next line in the file 
    student_list = [] # A list that will store each dictionary that contains student information 
    for i in infile: # Travreses the line of the file 
        word_list = i.strip().split(',') # Gets rid of extra spaced and seperates each information with a comma 
        if school_name == word_list[0]: # If the entered school name matches the school name from the file 
            # Stores the information of each student in the dictionary 
            dictionary = {'Age': int(word_list[1]), 'StudyTime': float(word_list[2]), 'Failures': int(word_list[3]), 'Health': int(word_list[4]), 'Absences': int(word_list[5]), 'G1': int(word_list[6]), 'G2': int(word_list[7]), 'G3': int(word_list[8])}
            student_list.append(dictionary) # Appends it to the list 
    infile.close() # Closes the file 
    return student_list # Returns the list of dictionaries containing the student info from the specified school 

# Do NOT include a main script in your submission
