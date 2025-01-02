# ECOR 1042 Deliverable 2 - Individual submission for test1 function

#import check module here

import check 

#import load_data module here

from load_data import student_school_list
from load_data import student_health_list
from load_data import student_age_list
from load_data import student_failures_list
from load_data import load_data
from load_data import add_average

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Rami Ayoub"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101261583"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T130"

#==========================================#
#Do not modify the code alreayd provided.

def test_return_list():
    
#test that student_school_list returns a list (3 different test cases required)
    check.equal(type(student_school_list('student-test.csv', 'GP')), list)
    check.equal(type(student_school_list('student-test.csv', 'MB')), list)
    check.equal(type(student_school_list('student-test.csv', 'CF')), list)
  
#test that student_age_list returns a list (3 different test cases required)
    check.equal(type(student_age_list('student-test.csv', 18)), list)
    check.equal(type(student_age_list('student-test.csv', 16)), list)
    check.equal(type(student_age_list('student-test.csv', 17)), list)

#test that student_health_list returns a list (3 different test cases required)
    check.equal(type(student_health_list('student-test.csv', 4)), list)
    check.equal(type(student_health_list('student-test.csv', 3)), list)
    check.equal(type(student_health_list('student-test.csv', 5)), list)
    
#test that student_failures_list returns a list (3 different test cases required)
    check.equal(type(student_failures_list('student-test.csv', 0)), list)
    check.equal(type(student_failures_list('student-test.csv', 2)), list)
    check.equal(type(student_failures_list('student-test.csv', 1)), list)
    
#test that load_data returns a list (6 different test cases required)
    check.equal(type(load_data('student-test.csv', ('All', -2))), list)
    check.equal(type(load_data('student-test.csv', ('School', 'GP'))), list)
    check.equal(type(load_data('student-test.csv', ('Failures', 0))), list)
    check.equal(type(load_data('student-test.csv', ('Age', 19))), list)
    check.equal(type(load_data('student-test.csv', ('Health', 3))), list)
    check.equal(type(load_data('student-test.csv', ('Failures', 2))), list)
    
#test that add_average returns a list (3 different test cases required)
    check.equal(type(add_average(load_data('student-test.csv', ('All', -2)))), list)
    check.equal(type(add_average(student_school_list('student-test.csv', 'MS'))), list)
    check.equal(type(add_average(student_health_list('student-test.csv', 1))), list)
    check.equal(type(add_average(student_age_list('student-test.csv', 15))), list)
    
    check.summary()

# Do NOT include a main script in your submission
