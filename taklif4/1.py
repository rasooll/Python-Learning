def create_grades_dict(file_name):
    my_dictionary = {}
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    for line in data:
        student_row = map(str.strip, line.strip().split(','))
        student_id = student_row.pop(0)
        student_lastname = student_row.pop(0)
        student_data = [student_lastname]
        for valid_test in ['Test_1', 'Test_2', 'Test_3', 'Test_4']:
            if valid_test in student_row:
                student_data.append(int(student_row[student_row.index(valid_test) + 1]))
            else:
                student_data.append(0)
        student_data.append(sum(student_data[-4: ])/4)        
        my_dictionary[student_id] = student_data
    return my_dictionary