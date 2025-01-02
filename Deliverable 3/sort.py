# ECOR 1042 Deliverable 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Rami Ayoub, Adam Rickert, Mazhar Kutukcu, Declan Foshaug"

# Update "" with your team (e.g. T102)
__team__ = "T-130"

#==========================================#
# Place your sort_students_age_bubble function after this line

def sort_students_age_bubble(age_dictionary: list[dict], ascend_descend_order: str) -> list[dict]:
    """Returns a list of dictionaries in ascending or decsending order specified by the user through 'A' or 'D' If the list of
    dictionaries key contains 'Age'. If the key is not withing the dicionary list it returns a message to the
    user indicating the key is not present and returns the list. 
    
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


#==========================================#
# Place your sort_students_time_selection function after this line

def sort_students_time_selection(time_dict: list[dict], arrangement: str) -> list[dict]:
    """Returns the given list of student's study time in the arrangement determined by the user. If the key is not present in the 
    list of dictionary then it returns a message to the user inicitaing that and returns the list. 

    >>> sort_students_time_selection([{"StudyTime":19.1,"School":"MS"}, {"StudyTime":10.2,"School":"GP"}], "A")
    
    [{'StudyTime': 10.2, 'School': 'GP'}, {'StudyTime': 19.1, 'School': 'MS'}]
    
    >>> sort_students_time_selection([{"StudyTime":10.2,"School":"GP"}, {"StudyTime":19.1,"School":"MS"}], "D")
    
    [{'StudyTime': 19.1, 'School': 'MS'}, {'StudyTime': 10.2, 'School': 'GP'}]
    
    >>> sort_students_time_selection([{"School":"MS"}, {"School":"GP"}], "A")
    
    "StudyTime" key is not present.
    [{'School': 'MS'}, {'School': 'GP'}]
    
    >>> sort_students_time_selection([{"StudyTime": 10.2,"School":"MS"}, {"StudyTime": 19.1,"School":"GP"}], "G")
    
    Arrangement input incompatible, please input either "A" or "D" for Ascending or Descending respectively
    """
    for x in time_dict:
        if 'StudyTime' not in x:
            print('"StudyTime" key is not present.')
            return time_dict
        else:

            if arrangement == "D":
                for x in range(len(time_dict)):
                    min_idx = x
                    for y in range(x + 1, len(time_dict)):
                        if time_dict[min_idx].get("StudyTime") < time_dict[y].get("StudyTime"):
                            min_idx = y

                        time_dict[x], time_dict[min_idx] = time_dict[min_idx], time_dict[x]

                return time_dict

            elif arrangement == "A":
                for x in range(len(time_dict)):
                    min_idx = x
                    for y in range(x + 1, len(time_dict)):
                        if time_dict[min_idx].get("StudyTime") > time_dict[y].get("StudyTime"):
                            min_idx = y

                        time_dict[x], time_dict[min_idx] = time_dict[min_idx], time_dict[x]

                return time_dict

            else:
                print('Arrangement input incompatible, please input either "A" or "D" for Ascending or Descending respectively')
                return


#==========================================#
# Place your sort_students_g_avg_insertion function after this line

def sort_students_g_avg_insertion (students:(list[dict]), rank:str) -> list[dict]:
    """Returns a list of dictionaries in ascending or decsending order specified by the user through 'A' or 'D' If the list of
    dictionaries key contains 'G_Avg'. If the key is not withing the dicionary list it returns a message to the
    user indicating the key is not present and returns the list. 
    
>>> sort_students_g_avg_insertion([{"G_Avg":7.2,"School":"GP"},
{"G_Avg":9.1,"School":"MS"}], "D")

[{'G_Avg': 9.1, 'School': 'MS'}, {'G_Avg': 7.2, 'School': 'GP'}]

>>> sort_students_g_avg_insertion([{"G_Avg":7.2,"School":"GP"},
{"G_Avg":9.1,"School":"MS"}], "A")

[{'G_Avg': 7.2, 'School': 'GP'}, {'G_Avg': 9.1, 'School': 'MS'}]

>>> sort_students_g_avg_insertion([{"School":"GP"},{"School":"MS"}], "D")

"G_Avg" key is not present
[{"School":"GP"}, {"School":"MS"}]
    """
    for x in students:
        if 'G_Avg' not in x:
            print ("'G_Avg' key is not present")
            return students         
         
    for i in range(1, len(students)):
        key = students[i]
        j = i-1
        if rank == 'A':
            while j>= 0 and students[j]['G_Avg']> key['G_Avg']:
                students[j+1] = students[j]
                j -= 1
        else:
            while j>= 0 and students[j]['G_Avg']< key['G_Avg']:
                students[j+1] = students[j]
                j -=1
        students[j+1] = key
    return students


#==========================================#
# Place your sort_students_failures_bubble function after this line

def sort_students_failures_bubble(failures_dictionary: list[dict], ascend_descend_order: str) -> list[dict]:
    """Returns a list of dictionaries in ascending or decsending order specified by the user through 'A' or 'D' If the list of
    dictionaries key contains 'Failures'. If the key is not withing the dicionary list it returns a message to the
    user indicating the key is not present and returns the list. 
    
>>> sort_students_failures_bubble([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D")
[{'Failures': 19, 'School': 'MS'}, {'Failures': 10, 'School': 'GP'}]

>>> sort_students_failures_bubble([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "A")
[{'Failures': 10, 'School': 'GP'}, {'Failures': 19, 'School': 'MS'}]

>>> sort_students_failures_bubble([{"School":"GP"}, {"School":"MS"}], "D")

"Failures" key is not present.
[{'School': 'GP'}, {'School': 'MS'}]
    """
    for x in failures_dictionary:
        if 'Failures' not in x: 
            print('"Failures" key is not present.')
            return failures_dictionary
    
    if ascend_descend_order.upper() == 'A':
        swap = True
        while swap:
            swap = False
            for i in range(len(failures_dictionary) - 1): 
                if failures_dictionary[i].get('Failures', 0) > failures_dictionary[i + 1].get('Failures', 0): 
                    failures_dictionary[i] = failures_dictionary[i + 1]
                    failures_dictionary[i + 1] = highest
                    swap = True
        
    elif ascend_descend_order.upper() == 'D':
        swap = True
        while swap:
            swap = False
            for i in range(len(failures_dictionary) - 1):
                if failures_dictionary[i].get('Failures', 0) < failures_dictionary[i + 1].get('Failures', 0):
                    highest = failures_dictionary[i]
                    failures_dictionary[i] = failures_dictionary[i + 1]
                    failures_dictionary[i + 1] = highest
                    swap = True 
                    
    return failures_dictionary

#==========================================#
# Place your sort function after this line

def sort_by_key(list_dictionary: list[dict], ascend_descend_order: str, dict_key: str) -> list[dict]: 
    """Returns a list of dictionaries in ascending or decsending order specified by the user through 'A' or 'D' If the list of
    dictionaries keys contain 'Age', 'StudyTime', 'G_Avg' or 'Failures'. If the key is not withing the dicionary list it returns a message to the
    user indicating the list cannot be sorted with that key and returns a list.
    
>>> sort_by_key([{"StudyTime":19.1,"School":"MS"}, {"StudyTime":10.2,"School":"GP"}], 'A', 'StudyTime')
[{'StudyTime': 10.2, 'School': 'GP'}, {'StudyTime': 19.1, 'School': 'MS'}]

>>> sort_by_key([{"Age":10,"School":"GP"}, {"Age":19,"School":"MS"}], 'D', 'Age') 
[{'Age': 19, 'School': 'MS'}, {'Age': 10, 'School': 'GP'}]

>>> sort_by_key([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D", 'Failures')
[{'Failures': 19, 'School': 'MS'}, {'Failures': 10, 'School': 'GP'}]

>>> sort_by_key([{"G_Avg":7.2,"School":"GP"}, {"G_Avg":9.1,"School":"MS"}], "A", 'G_Avg')
[{'G_Avg': 7.2, 'School': 'GP'}, {'G_Avg': 9.1, 'School': 'MS'}]

>>> sort_by_key([{"School":"GP"}, {"School":"MS"}], "D", "School")

Cannot be sorted by 'School'
[{"School":"GP"}, {"School":"MS"}]
    """
    if dict_key == 'Age':
        new_list_dictionary = sort_students_age_bubble(list_dictionary, ascend_descend_order)
        
    elif dict_key == 'StudyTime':
        new_list_dictionary = sort_students_time_selection(list_dictionary, ascend_descend_order)
        
    elif dict_key == 'G_Avg':
        new_list_dictionary = sort_students_g_avg_insertion(list_dictionary, ascend_descend_order)
        
    elif dict_key == 'Failures':
        new_list_dictionary = sort_students_failures_bubble(list_dictionary, ascend_descend_order)
        
    else:
        print(f"Cannot be sorted by '{dict_key}'")
        return list_dictionary
        
    return new_list_dictionary

# Do NOT include a main script in your submission
