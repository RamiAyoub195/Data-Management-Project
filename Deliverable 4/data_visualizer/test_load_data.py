# ECOR 1042 Lab 4 - team submission

#import check module here

import check

#import load_data module here

from load_data import student_school_list
from load_data import student_health_list
from load_data import student_age_list
from load_data import student_failures_list
from load_data import load_data
from load_data import add_average

# Update "" with your the name of the active members of the team
__author__ = "Rami Ayoub, Adam Rickert, Declan Foshaug, Ali Mazhar"

# Update "" with your student number (e.g., 100100100)

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-130"

#==========================================#

# Place test_return_list function here 

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

# Place test_return_list_correct_lenght function here

def test_return_list_correct_lenght():
    
#test that student_school_list returns a list with the correct lenght (3 different test cases required)
    
    check.equal(len(student_school_list('student-test.csv', 'GP')), 3)
    check.equal(len(student_school_list('student-test.csv', 'CU')), 0)
    check.equal(len(student_school_list('student-test.csv', 'MB')), 2)
    
#test that student_age_list returns a list  with the correct lenght (3 different test cases required)
    
    check.equal(len(student_age_list('student-test.csv', 18)), 4)
    check.equal(len(student_age_list('student-test.csv', 11)), 0)
    check.equal(len(student_age_list('student-test.csv', 17)), 6)
        
#test that student_health_list returns a list  with the correct lenght (3 different test cases required)
    
    check.equal(len(student_health_list('student-test.csv', 3)), 8)
    check.equal(len(student_health_list('student-test.csv', 0)), 0)
    check.equal(len(student_health_list('student-test.csv', 1)), 1)
    
#test that student_failures_list returns a list   with the correct lenght(3 different test cases required)
    
    check.equal(len(student_failures_list('student-test.csv', 0)), 11)
    check.equal(len(student_failures_list('student-test.csv', 3)), 1)
    check.equal(len(student_failures_list('student-test.csv', 6)), 0)
    
#test that load_data returns a list  with the correct lenght (6 different test cases required)
    
    check.equal(len(load_data('student-test.csv', ('School', 'CF'))), 3)
    check.equal(len(load_data('student-test.csv', ('Failures', 0))), 11)
    check.equal(len(load_data('student-test.csv', ('Age', 19))), 0)
    check.equal(len(load_data('student-test.csv', ('Health', 3))), 8)
    check.equal(len(load_data('student-test.csv', ('All', -3))), 15)
    check.equal(len(load_data('student-test.csv', ('School', 'MS'))), 4)
    
#test that add_average returns a list   with the correct lenght (3 different test cases required)
    
    check.equal(len(add_average(load_data('student-test.csv', ('All', -3)))), 15)
    check.equal(len(add_average(student_school_list('student-test.csv', 'CF'))), 3)
    check.equal(len(add_average(student_age_list('student-test.csv', 15))), 3)
    check.equal(len(add_average(student_failures_list('student-test.csv', 0))), 11)
    
    check.summary()

#Place test_return_correct_dict_inside_list function here
def test_return_correct_dict_inside_list():
    
#test that student_school_list returns a correct dictionary inside the list (3 different test cases required)
    
    check.equal(student_school_list('student-test.csv', 'GP'), [{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, {'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}])
    
    check.equal(student_school_list('student-test.csv', 'MB'), [{'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}])
    
    check.equal(student_school_list('student-test.csv', 'CF'), [{'Age': 15, 'StudyTime': 5.0, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}, {'Age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}, {'Age': 17, 'StudyTime': 1.0, 'Failures': 2, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0}])
    
    check.equal(student_school_list('student-test.csv', 'CU'), [])
    
#test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)
    
    check.equal(student_age_list('student-test.csv', 18), [{'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'BD', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 8}, {'School': 'BD', 'StudyTime': 3.0, 'Failures': 0, 'Health': 3, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12}, {'School': 'MS', 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}] )
    
    check.equal(student_age_list('student-test.csv', 15), [{'School': 'GP', 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {'School': 'MB', 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}, {'School': 'CF', 'StudyTime': 5.0, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}])
                
    check.equal(student_age_list('student-test.csv', 16), [{'School': 'MB', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'CF', 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}])
    
#test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)
    
    check.equal(student_health_list('student-test.csv', 1), [{'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9}])
    
    check.equal(student_health_list('student-test.csv', 4), [{'School': 'BD', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 10, 'G2': 9, 'G3': 9}, {'School': 'MS', 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 8, 'G1': 11, 'G2': 10, 'G3': 10}, {'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}])
    
    check.equal(student_health_list('student-test.csv', 5), [{'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}, {'School': 'CF', 'Age': 17, 'StudyTime': 1.0, 'Failures': 2, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0}, {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}]) 
    
    check.equal(student_health_list('student-test.csv', 7), [])
    
#test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
    
    check.equal(student_failures_list('student-test.csv', 3), [{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}])
    
    check.equal(student_failures_list('student-test.csv', 1), [{'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}])
    
    check.equal(student_failures_list('student-test.csv', 2), [{'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}, {'School': 'CF', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0}])

#test that load_data returns a correct dictionary inside the list (6 different test cases required)
    
    check.equal(load_data('student-test.csv', ('All', -3)), [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {'School': 'MB', 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'MB', 'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}, {'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}, {'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}, {'School': 'CF', 'Age': 17, 'StudyTime': 1.0, 'Failures': 2, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0}, {'School': 'BD', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 8}, {'School': 'BD', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 3, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12}, {'School': 'BD', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 4, 'G1': 10, 'G2': 9, 'G3': 9}, {'School': 'MS', 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Health': 4, 'Absences': 8, 'G1': 11, 'G2': 10, 'G3': 10}, {'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 1, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9}, {'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}, {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}]
)
    
    check.equal(load_data('student-test.csv', ('School', 'MB')), [{'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}])
    
    check.equal(load_data('student-test.csv', ('Failures', 1)), [{'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}])
    
    check.equal(load_data('student-test.csv', ('Health', 5)), [{'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}, {'School': 'CF', 'Age': 17, 'StudyTime': 1.0, 'Failures': 2, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0}, {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])
    
    check.equal(load_data('student-test.csv', ('Age', 16)), [{'School': 'MB', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'CF', 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}])
    
    check.equal(load_data('student-test.csv', ('School', 'BD')), [{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 8}, {'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 3, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12}, {'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 4, 'G1': 10, 'G2': 9, 'G3': 9}])
    
    check.equal(load_data('student-test.csv', ('Failures', 9)), [])
    
    #test that add_average returns a lcorrect dictionary inside the list  (3 different test cases required)
   
    check.equal(add_average(student_school_list('student-test.csv', 'MB')), [{'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5, 'G_Avg': 5.0}, {'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12, 'G_Avg': 11.33}])
   
    check.equal(add_average(student_health_list('student-test.csv', 1)), [{'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9, 'G_Avg': 9.33}])
   
    check.equal(add_average(student_failures_list('student-test.csv', 2)), [{'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7, 'G_Avg': 7.0}, {'School': 'CF', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0, 'G_Avg': 4.33}])
    
    check.summary()

#Place test_add_average function here

def test_add_average():
    
    #test that the function does not change the lengh of the list provided as input parameter (5 different test cases required)
    
    check.equal(len(add_average(student_school_list('student-test.csv', 'MB'))), 2)
    check.equal(len(add_average(student_age_list('student-test.csv', 16))), 2)
    check.equal(len(add_average(student_failures_list('student-test.csv', 0))), 11)
    check.equal(len(add_average(student_health_list('student-test.csv', 3))), 8)
    check.equal(len(add_average(load_data('student-test.csv', ('All', -1)))), 15)
   
    #test that the function returns an empty list when it is called whith an empty list
    
    check.equal(len(add_average(student_school_list('student-test.csv', 'CU'))), 0)   
    
    #test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)
    
    previous_key_length = 8
    previous_key_length_all = 9
    new_keys_length_1 = add_average(student_age_list('student-test.csv', 16))
    new_keys_length_2 = add_average(load_data('student-test.csv', ('All', -1)))
    new_keys_length_3 = add_average(student_health_list('student-test.csv', 1))
    new_keys_length_4 = add_average(student_failures_list('student-test.csv', 3))
    new_keys_length_5 = add_average(student_school_list('student-test.csv', 'GP'))
    
    check.equal(len(new_keys_length_1[0].keys()), previous_key_length + 1)
    check.equal(len(new_keys_length_2[0].keys()), previous_key_length_all + 1)
    check.equal(len(new_keys_length_3[0].keys()), previous_key_length + 1)
    check.equal(len(new_keys_length_4[0].keys()), previous_key_length + 1)
    check.equal(len(new_keys_length_5[0].keys()), previous_key_length + 1)
    
    #test that the G_Avg value is properly calculated  (5 different test cases required)
    
    g_average_test_1 = add_average(student_age_list('student-test.csv', 17))
    G_Avg_1 = g_average_test_1[0].get('G_Avg', 0)
    
    g_average_test_2 = add_average(load_data('student-test.csv', ('All', -1)))
    G_Avg_2 = g_average_test_2[0].get('G_Avg', 0)
    
    g_average_test_3 = add_average(student_health_list('student-test.csv', 1))
    G_Avg_3 = g_average_test_3[0].get('G_Avg', 0) 
    
    g_average_test_4 = add_average(student_school_list('student-test.csv', 'BD'))
    G_Avg_4 = g_average_test_4[0].get('G_Avg', 0)
    
    g_average_test_5 = add_average(student_failures_list('student-test.csv', 1))
    G_Avg_5 = g_average_test_5[0].get('G_Avg', 0)
    
    check.equal(G_Avg_1, 5.33)
    check.equal(G_Avg_2, 5.67)
    check.equal(G_Avg_3, 9.33)
    check.equal(G_Avg_4, 8.0)
    check.equal(G_Avg_5, 11.33)
    
    check.summary()

# Do NOT include a main script in your submission
