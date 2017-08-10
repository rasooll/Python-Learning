def print_grades(file_name):
    di=create_grades_dict(file_name)
    keys=di.keys()
    values=di.values()
    print()
    s='    ID     |       Name       | Test_1 | Test_2 | Test_3 | Test_4 |  Avg.  |\n'
    for i in sorted(keys):
        d='{0:<10s} | {1:<16s} | {2:>6d} | {3:>6d} | {4:>6d} | {5:>6d} | {6:>6.2f} |\n'.format(i,di[i][0],di[i][1],di[i][2],di[i][3],di[i][4],di[i][5])
        s=s+d
    s=s.rstrip('\n')
    print (s)