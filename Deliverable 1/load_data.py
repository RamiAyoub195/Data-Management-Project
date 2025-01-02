# ECOR 1042 Deliverable 1 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Rami Ayoub, Declan Foshaug , Adam Rickert, Mazhar Kutukcu"

# Update "" with your team (e.g. T102)
__team__ = "T130"

#==========================================#
# Place your student_school_list function after this line

def student_school_list(file_name: str, school_name: str) -> list[dict]:
    """Returns a list of dictionaries for several students, the dictionary includes
    student age, studytime, failure, health, absences, G1 (first period grade), G2(second
    period grade) and G(final grade) for a chosen school. If a school is not found in the
    data, an empty list is returned.
    
    Precondition: None
    
>>> student_school_list('student-mat.csv', 'GP')
    [{'Age': 18, 'StudyTime': 2.0, 'Failure': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}]
    
>>> student_school_list('student-mat.csv', 'MB')
    [{'Age': 16, 'StudyTime': 2.0, 'Failure': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {another element}]
    
>>> student_school_list('student-mat.csv', 'CU')
    []
    """
    infile = open(file_name, 'r')
    next(infile)
    student_list = []
    for i in infile:
        word_list = i.strip().split(',')
        if school_name == word_list[0]:
            dictionary = {'Age': int(word_list[1]), 'StudyTime': float(word_list[2]), 'Failure': int(word_list[3]), 'Health': int(word_list[4]), 'Absences': int(word_list[5]), 'G1': int(word_list[6]), 'G2': int(word_list[7]), 'G3': int(word_list[8])}
            student_list.append(dictionary)
    infile.close()
    return student_list 

#==========================================#
# Place your student_health_list function after this line

def student_health_list(file_name: str, student_health: int) -> list[dict]:
    """Returns a list of dictionaries containg the following information about students, 'School, 'Age', 'StudyTime', 'Failures', 
    'Absences', 'G1', 'G2', 'G3' when entering a file and the student's asscoiated health.
    
    Precondition: None

>>> student_health_list('student-mat.csv', 1)
[{'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': '6', 'G2': '5', 'G3': '6'}, {another element}]

>>> student_health_list('student-mat.csv', 3)
[{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': '5', 'G2': '6', 'G3': '6'}, {another element}]

>>> student_health_list('student-mat.csv', 7)
[]
    """
    infile = open(file_name, "r")
    next(infile)
    health = []

    for i in infile:
        word_list = i.strip().split(',')
        
        if student_health == int(word_list[4]):
            dictionary = {'School': str(word_list[0]), 'Age': int(word_list[1]), 'StudyTime': float(word_list[2]), 'Failures': int(
            word_list[3]), 'Absences': int(word_list[5]), 'G1': (word_list[6]), 'G2': (word_list[7]), 'G3': (word_list[8])}
            health.append(dictionary)

    infile.close()

    return health

#==========================================#
# Place your student_age_list function after this line

def student_age_list(file: str, age: int) -> list[dict]:
    """Returns a list of dictionaries containing the following data for students, 'School', 'StudyTime', 
    'Failures', 'Health', 'Absences', 'G1', 'G2', 'G3' when a file and specified student age is entered.
    
    Precondition: None
    
>>>student_age_list('student-mat.csv', 15)
[{'School': 'GP', 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {another element}}

>>> student_age_list('student-mat.csv', 17)
[{'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, {another element}]

>>> student_age_list('student-mat.csv', 13)
[]
    """
    infile = open(file, "r")
    next(infile)
    list_1 = []
    for line in infile: 
        student_age_list = line.strip().split(',')
        if age == int(student_age_list[1]):
            dictionary = {'School': student_age_list[0], 'StudyTime': float(student_age_list[2]), 'Failures': int(student_age_list[3]), 'Health':int(student_age_list[4]), 'Absences':int(student_age_list[5]), 'G1':int(student_age_list[6]), 'G2':int(student_age_list[7]), 'G3':int(student_age_list[8])}
            list_1.append(dictionary)
    
    infile.close()
    return list_1

#==========================================#
# Place your student_failures_list function after this line

def student_failures_list(filename: str, failures_int: int) -> list[dict]:
    infile = open(filename, 'r')
    next(infile)
    empty_list = []
    
    '''Returns the student information of students with the specified amount of failure
    >>> student_failures_list('student-mat.csv', 0)
[{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another
element}, ...]
    >>> student_failures_list('student-mat.csv', 3)
[{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {another
element}, ...]
    '''
    for failures in infile:
        word = failures.strip().split(',')
        
        if failures_int == int(word[3]):
            student_data = {'School': str(word[0]), 'Age': int(word[1]), 'StudyTime': float(word[2]), 'Health':
            int(word[4]), 'Absences': int(word[5]), 'G1': int(word[6]), 'G2': int(word[7]), 'G3': int(word[8])}
            empty_list.append(student_data)
            
    infile.close()
            
    return empty_list

#==========================================#
# Place your load_data function after this line

def load_data(student_file: str, data_student_filter: tuple) -> list[dict]:
    """Returns a list of dictionaries for the chosen data of the user, the user enters a
    file name and a tuple that includes a key such as 'Age', 'Failures', 'School', 'Health'
    or 'All' with an value for the key. If 'All' is choosen then the secod value in the tuple 
    is disregraded.
    
    Precondition: None
    
>>> load_data('student-mat.csv', ('All', -2))
[{'School': 'GP', 'Age': 18, 'Studytime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}]

>>> load_data('student-mat.csv', ('School', 'GP'))
[{'Age': 18, 'Studytime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}]

>>> load_data('student-mat.csv', ('Failures', 0))
[{'School': 'GP', 'Age': 18, 'Studytime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}

>>> load_data('student-mat.csv', ('Age', 12))
[]
    """
    file = open(student_file, "r")
    next(file)
    student_list = []
    
    for i in file:
        word_list = i.strip().split(',')
        if data_student_filter[0] == 'All':
            dictionary_1 = {'School': word_list[0], 'Age': int(word_list[1]), 'StudyTime': float(word_list[2]), 
                      'Failures': int(word_list[3]), 'Health': int(word_list[4]), 'Absences': int(word_list[5]), 
                      'G1': int(word_list[6]), 'G2': int(word_list[7]), 'G3': int(word_list[8])}
            student_list.append(dictionary_1)
    
        elif data_student_filter[0] == 'School' and data_student_filter[1] == word_list[0]:
            dictionary_2 = {'Age': int(word_list[1]), 'StudyTime': float(word_list[2]), 
                      'Failures': int(word_list[3]), 'Health': int(word_list[4]), 'Absences': int(word_list[5]), 
                      'G1': int(word_list[6]), 'G2': int(word_list[7]), 'G3': int(word_list[8])}
            student_list.append(dictionary_2)
            
        elif data_student_filter[0] == 'Age' and data_student_filter[1] == int(word_list[1]):
            dictionary_3 = {'School': word_list[0], 'StudyTime': float(word_list[2]), 
                      'Failures': int(word_list[3]), 'Health': int(word_list[4]), 'Absences': int(word_list[5]), 
                      'G1': int(word_list[6]), 'G2': int(word_list[7]), 'G3': int(word_list[8])}
            student_list.append(dictionary_3)
            
        elif data_student_filter[0] == 'Health' and data_student_filter[1] == int(word_list[4]):
            dictionary_4 = {'School': word_list[0], 'Age': int(word_list[1]), 'StudyTime': float(word_list[2]), 
                      'Failures': int(word_list[3]), 'Absences': int(word_list[5]), 
                      'G1': int(word_list[6]), 'G2': int(word_list[7]), 'G3': int(word_list[8])}
            student_list.append(dictionary_4)
            
        elif data_student_filter[0] == 'Failures' and data_student_filter[1] == int(word_list[3]):
            dictionary_5 = {'School': word_list[0], 'Age': int(word_list[1]), 'StudyTime': float(word_list[2]), 
                      'Health': int(word_list[4]), 'Absences': int(word_list[5]), 
                      'G1': int(word_list[6]), 'G2': int(word_list[7]), 'G3': int(word_list[8])}
            student_list.append(dictionary_5)  
            
    file.close()
            
    return student_list
       
#==========================================#
# Place your add_average function after this line

def add_average(student_list: list[dict]) -> list[dict]:
    """Returns a new list of dictionaries including the old dictionary with a new key called 'G_Avg', this key contains
    a value of the students overall average from the entries 'G1', 'G2', 'G3'. 
   
    Precondition: None
    
>>> add_average([{'Age': 16, 'StudyTime': 2.0, 'Failure': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {another element}])
[{'Age': 16, 'StudyTime': 2.0, 'Failure': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5, 'G_Avg': 5.0}, {another element}]

>>> add_average([{'Age': 15, 'StudyTime': 3.0, 'Failure': 0, 'Health': 5, 'Absences': 2, 'G1': 15, 'G2': 14, 'G3': 15}, {another element}])
[{'Age': 15, 'StudyTime': 3.0, 'Failure': 0, 'Health': 5, 'Absences': 2, 'G1': 15, 'G2': 14, 'G3': 15, 'G_Avg': 14.67}, {another element}]
    """
    average_value = 0
    new_student_list = []
    for i in student_list:
        G_1 = i.get('G1', 0)
        G_2 = i.get('G2', 0)
        G_3 = i.get('G3', 0)
        average_value = (G_1 + G_2 + G_3)/3
        x = {'G_Avg': round(average_value , 2)}
        i.update(x)
        new_student_list.append(i)
    return new_student_list
    
# Do NOT include a main script in your submission
