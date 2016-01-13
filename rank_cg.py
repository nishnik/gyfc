from bs4 import BeautifulSoup
import re
import sys

filePath_from = ""

if len(sys.argv) != 2:
    print "Usage: rank_cg.py <roll_no>"
    print "Example: rank_cg.py 7"
else:
    to_find = sys.argv[1]

    f = open(filePath_from + str(to_find), 'r')
    site_data = f.read()
    regex = "<b> CGPA</b></td><td>(.+?)</td>"
    pattern = re.compile(regex)
    to_find_cg = re.findall(pattern, site_data)
    rank = 1
    for i in range(1, 60):
        f = open(filePath_from + str(i), 'r')
        site_data = f.read()
        regex = "<b> CGPA</b></td><td>(.+?)</td>"
        pattern = re.compile(regex)
        cg = re.findall(pattern, site_data)
        if(len(cg) > 2):
            if to_find_cg[0] <= cg[0]:
                rank = rank + 1
    print rank - 1
