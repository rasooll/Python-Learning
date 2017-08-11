def calculate_grades(file_name):
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    students_list = []
    for each_line in data:
        name,quiz1,quiz2,quiz3,quiz4 = each_line.strip().split(',')
        quiz_average = (float(quiz1)+float(quiz2)+float(quiz3)+float(quiz4))/4
        students_list.append((name,quiz_average))
    
    
    unSorted = True
    while unSorted:
        unSorted = False
        for index in range(0, len(students_list)-1):
            # if next element is greater element then swap them
            if students_list[index][0] > students_list[index + 1][0]:
                temporary_variable = students_list[index]
                students_list[index] = students_list[index + 1]
                students_list[index + 1] = temporary_variable
                unSorted = True    
    my_tuple = tuple(students_list)
    return my_tuple