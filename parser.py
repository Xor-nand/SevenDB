import re

def linesof(file):
    f = open(file, "r")
    listline = f.readlines()
    f.close()
    return listline

def write(a):
    print(a)

def check(str, pattern):
    # _matching the strings
    if re.search(pattern, str):
        listofprods.append(str)
    else:
        trash.append(str)

file = "outputmail.txt"
listline = linesof(file)
listofprods = []
trash = []

pattern = re.compile('\d[.]\d+\s')

for i in listline:
     check('{}'.format(i), pattern)
