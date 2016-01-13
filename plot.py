from bs4 import BeautifulSoup
filePath_from = ""
filePath_to = ""

dict_grades = {}
subjects = []
for i in range(1, 60):
    print i
    f = open(filePath_from + str(i), 'r')
    site_data = f.read()
    soup = BeautifulSoup(site_data)
    for row in soup.find_all('tr', bgcolor=["pink", "#FFF3FF"]):
        if len(row) == 13:

            td = row.find_all('td')
            if(dict_grades.has_key((td[0].contents[0], td[4].contents[0]))):
                dict_grades[(td[0].contents[0], td[4].contents[0])] = dict_grades[
                    (td[0].contents[0], td[4].contents[0])] + 1
            else:
                dict_grades[(td[0].contents[0], td[4].contents[0])] = 1
            if td[0].contents[0] not in subjects:
                subjects.append(td[0].contents[0])

import numpy as np
import matplotlib.pyplot as plt
for no in range(len(subjects)):
    plt.figure()
    N = 8
    grades = (dict_grades.get((subjects[no], "EX"), 0),
              dict_grades.get((subjects[no], "A"), 0),
              dict_grades.get((subjects[no], "B"), 0),
              dict_grades.get((subjects[no], "C"), 0),
              dict_grades.get((subjects[no], "D"), 0),
              dict_grades.get((subjects[no], "P"), 0),
              dict_grades.get((subjects[no], "F"), 0),
              dict_grades.get((subjects[no], "X"), 0))
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, grades, width, color='r')

    plt.ylabel('Number of Students')
    plt.title('Grades in ' + subjects[no])
    plt.xticks(ind + width / 2., ('EX', 'A', 'B', 'C', 'D', 'P', 'F', 'X'))
    plt.savefig(filePath_to + subjects[no])


print subjects
