def my_final_grade_calculation(filename):
    fp = open(filename, "r")
    data = fp.readlines()
    my_dictionary = {}
    for x in range(0, len(data)):
        stripped = data[x].strip().split(',')
        for x in range(1, len(stripped)):
            stripped[x] = int(stripped[x].strip())

        # extract various parts from each line
        name = stripped[0].lower()
        quizzes = stripped[1:7]
        assignments = stripped[7:11]
        midterm = int(stripped[11])
        final = int(stripped[12])

        # deal with the quizzes # remove the two minimum quizzes
        quizzes.remove(min(quizzes))
        quizzes.remove(min(quizzes))

        # deal with the assignments # remove one of the minimum assignment
        assignments.remove(min(assignments))

        # calculate the percentage of each score based on 25%
        quiz_score = (sum(quizzes)/len(quizzes)) * 0.25
        assignment_score = (sum(assignments)/len(assignments)) * 0.25
        midterm_score = midterm * 0.25
        final_score = final * 0.25

        # calculate total score
        total_score = quiz_score + midterm_score + assignment_score + final_score
        # print("q =", quizzes, quiz_score)
        # print("assign =", assignments, assignment_score)
        # print("midterm, final", midterm_score, final_score)
        # print("total_score", total_score)
        if total_score >= 60:
            my_dictionary[name] = "pass"
        else:
            my_dictionary[name] = "fail"
    return my_dictionary